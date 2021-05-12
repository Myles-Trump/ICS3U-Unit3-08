#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user input the year to determine
#   if it is a leap year or not


def main():
    # this function lets the user input the year to determine
    #   if it is a leap year or not

    # input
    year = input("Enter a year (integer): ")

    # process & output
    try:
        year_int = int(year)

        if 0 != year_int % 4:
            print("\nYour year, {0}, is not a leap year.".format(year_int))

        elif 0 != year_int % 100:
            print("\nYour year, {0}, is a leap year.".format(year_int))

        elif 0 != year_int % 400:
            print("\nYour year, {0}, is not a leap year.".format(year_int))

        else:
            print("\nYour year, {0}, is a leap year.".format(year_int))

    except Exception:
        print("\n{0} is not a valid integer.".format(year))

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
