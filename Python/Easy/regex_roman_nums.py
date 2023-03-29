import re

# reference https://en.wikipedia.org/wiki/Roman_numerals for info on notation
thous = r"(M{0,3})"
hund = r"(D?[C]{0,3}|C[DM])"
ten = r"(L?[X]{0,3}|X[LC])"
one = r"(V?[I]{0,3}|I[VX])"

regex_pattern = r"^" + thous + hund + ten + one + r"$"
print(str(bool(re.match(regex_pattern, input()))))
