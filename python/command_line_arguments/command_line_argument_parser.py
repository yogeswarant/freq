import argparse
import os, sys
g_version = "1.0"

def parse_arguments():
    global g_version
    args = argparse.ArgumentParser(description = 'Agrument Parser Example v%s' % g_version)
    args.add_argument('-m', '--metafile', default=os.path.join(os.getcwd(), 'reporter.cfg'))
    args.add_argument('-e', '--enable', action='store_true')
    args.add_argument('-o', '--outputdir', default=os.getcwd())
    args.add_argument('-s', '--sendmail', default='')
    args.add_argument('-g', '--groupby', default='NONE', choices=['PROGRAM', 'TYPE', 'NONE'])
    args.add_argument('-v', '--version', action='version', version="%s %s" % (sys.argv[0], g_version))
    return args.parse_args()

def main():
	args = parse_arguments()
	print 'Metafile:', args.metafile
	print 'Enable:', args.enable
	print 'Outputdir:', args.outputdir
	print 'Sendmail:', args.sendmail
	print 'Groupby:', args.groupby
	print "\n"
	print args


if __name__ == '__main__':
	main()
