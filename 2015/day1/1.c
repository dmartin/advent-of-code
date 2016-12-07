#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char const *argv[]) {
	if (argc > 1) {
		FILE* input = fopen(argv[1], "r");
		if (!input) {
			perror("Could not open file");
			return EXIT_FAILURE;
		}
		int c;
		int charpos = 0;
		int flr = 0;
		bool entered_basement = false;
		while ((c = fgetc(input)) != EOF) {
			charpos = charpos + 1;
			if (c == '(') {
				flr = flr + 1;
			}
			else if (c == ')') {
				flr = flr - 1;
			}
			if (flr == -1 && entered_basement == false) {
				entered_basement = true;
				printf("%s%u\n", "First entered basement at char ", charpos);
			}
		}
		printf("%s%u\n", "Floor ", flr);
	}
	return 0;
}
