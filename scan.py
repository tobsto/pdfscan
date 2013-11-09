#!/usr/bin/python

import argparse
import subprocess
import os

def run(cmd, log):
	#print cmd
	logfile=log + ".log"
	error_logfile=log + ".err"
	# append logs to logfiles
	fstdout = open(logfile, 'a')
	fstderr = open(error_logfile, 'a')

	# run job
	process=subprocess.Popen(cmd, shell=True, stdout=fstdout, stderr=fstderr)
	fstdout.close()
	fstderr.close()
	process.communicate()
	status=process.returncode
	print status
	if status!=0:
		print "Error while executing"
		print cmd
		print "Stdout:"
		subprocess.call("cat " + logfile, shell=True)
		print "Stderr:"
		subprocess.call("cat " + error_logfile, shell=True)
		print "Break"
		exit(1)
	
def scan_page(page, color, brightness_contrast, log):
	home=os.environ['HOME']
	# perl script for scanning 
	print "scanning page %s ..." % page
	cmd="sudo %s/Sonstiges/Programme/scanner/canoscan600f-20130118.pl" % home
	run(cmd,log)
	# convert to pdf
	cmd="convert scan.ppm -colorspace %s -brightness-contrast %s temp.pdf" % (color, brightness_contrast)
	run(cmd,log)
	# reduce size
	cmd="gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=temp_%03i.pdf temp.pdf" % page
	run(cmd,log)
	# remove temporary file
	cmd="rm -f temp.pdf temp.ppm"
	run(cmd,log)

def main():
	parser = argparse.ArgumentParser(description='Scan several pages and merge them into a single pdf file')
        parser.add_argument('-o', '--output', default="scan.pdf", help='output file name')
        parser.add_argument('-p', '--pages', default=1, help='number of pages to scan', type=int)
        parser.add_argument('-b', '--brightness_contrast', default="50x40", help='brightness contrast option for imagemagick')
        parser.add_argument('-c', '--color', default="Gray", help='colorspace option for imagemagick')

	args = parser.parse_args()

	home=os.environ['HOME']
	log="%s/Sonstiges/Programme/scanner/scan" % home

	subprocess.call("sudo echo", shell=True)
	for page in range(1,args.pages+1):
		raw_input("Put page %i into the scanner and hit any key" % page)
		scan_page(page, args.color, args.brightness_contrast, log)
	if args.pages==1:
		cmd="mv temp_001.pdf " +  args.output
		run(cmd,log)
	else:
		cmd="pdfjoin "
		for page in range(1,args.pages+1):
			cmd=cmd + "temp_%03i.pdf " % page
		cmd=cmd + args.output
		run(cmd,log)
		

if __name__=="__main__":
        main()
