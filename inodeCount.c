#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>
#include <stdlib.h>

/* get length of array */
#define NELEMS(x)  (sizeof(x) / sizeof((x)[0]))

long inodeCount(const char *name, int level, int maxDepth) {

	DIR *dir;
	struct dirent *entry;
	long local = 0, total = 0;
	
	if(!(dir = opendir(name)))
		return;
	if(!(entry = readdir(dir)))
		return;

	do { 

		if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
			continue;

		local++;

		if(entry->d_type == DT_DIR) {
			char path[1024];
			long len = snprintf(path, sizeof(path)-1, "%s/%s", name, entry->d_name);
			path[len] = 0;
			total += inodeCount(path, level + 1, maxDepth);
        }

	} while (entry = readdir(dir));

	total += local;
	closedir(dir);
	if(maxDepth) {
		if(level < maxDepth)
			printf("%s: %d\n", name, total);
		}
	return total;
}

int main(int argc, const char *const *argv) {

	if(argc < 2) {
		printf("Usage: %s path [ depth (max depth to print dir totals ]\n",argv[0]);
		exit(1);
	}

	long total = 1;
	const char *path = argv[1];
	long maxDepth = 0;

	if(argc == 3) 
		maxDepth = strtol(argv[2], NULL, 10);

	total += inodeCount(path, 0, maxDepth);
	printf("Grand total: %d\n", total);
	return 0;
}
