#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates exactly 5 zombie processes, then rins an inf while func
 *
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			sleep(0.1);
		if (pid == 0)
		{
			printf("Zombie process created, PID: %u\n", pid);
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
