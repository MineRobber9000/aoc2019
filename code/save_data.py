import aocd, argparse

parser = argparse.ArgumentParser(description="Saves AOCD input to a file")
parser.add_argument("-y","--year",default=None,help="The year of the puzzle")
parser.add_argument("day",help="Day of the puzzle.",type=int)
args = parser.parse_args()

with open("data.txt","w") as f:
	f.write(aocd.get_data(day=args.day,year=(int(args.year) if args.year is not None else args.year)))
