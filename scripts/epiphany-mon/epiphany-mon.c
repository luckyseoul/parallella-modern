/*
 * epiphany-mon - Lightweight Epiphany mesh monitor
 * Supports E16 (16 cores) and E64 (64 cores)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ncurses.h>

#define MAX_CORES 64
#define BAR_WIDTH 10

typedef struct {
    int core_id;
    int usage;      // 0-100
} core_status_t;

int num_cores = 16;  // default to E16

void draw_bar(int usage) {
    int filled = (usage * BAR_WIDTH) / 100;
    addch('[');
    for (int i = 0; i < BAR_WIDTH; i++) {
        if (i < filled)
            addch(ACS_CKBOARD);
        else
            addch(' ');
    }
    addch(']');
    printw(" %3d%%", usage);
}

void draw_mesh(core_status_t cores[]) {
    clear();
    attron(A_BOLD);
    printw("Epiphany Mesh Utilization (%d cores)\n\n", num_cores);
    attroff(A_BOLD);

    int cols = 4;
    int rows = (num_cores + cols - 1) / cols;

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            int idx = row * cols + col;
            if (idx >= num_cores) break;

            printw("Core %2d ", idx);
            draw_bar(cores[idx].usage);
            printw("   ");
        }
        printw("\n");
    }

    printw("\n");
    printw("Press 'q' to quit\n");
    refresh();
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        num_cores = atoi(argv[1]);
        if (num_cores < 1 || num_cores > MAX_CORES)
            num_cores = 16;
    }

    core_status_t cores[MAX_CORES] = {0};

    initscr();
    cbreak();
    noecho();
    nodelay(stdscr, TRUE);
    curs_set(0);

    int ch;
    while (1) {
        // Simulate usage (replace with real shared memory reads later)
        for (int i = 0; i < num_cores; i++) {
            cores[i].usage = (rand() % 60) + 20;  // fake data
        }

        draw_mesh(cores);

        ch = getch();
        if (ch == 'q' || ch == 'Q')
            break;

        sleep(1);
    }

    endwin();
    return 0;
}