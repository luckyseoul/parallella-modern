/*
 * Parallel Explorer Core
 * Runs independently on each Epiphany core.
 * Generates ideas / solutions in parallel.
 */

#include <stdio.h>
#include "e_lib.h"

#define MAX_IDEAS 32
#define IDEA_LEN  128

typedef struct {
    char ideas[MAX_IDEAS][IDEA_LEN];
    int count;
} explorer_state_t;

int main(void) {
    explorer_state_t *state = (explorer_state_t *)0x8f000000; // shared memory example

    state->count = 0;

    // Placeholder loop - each core will eventually have different prompts/strategies
    for (int i = 0; i < 8; i++) {
        // In reality this would call a small model or use templates
        snprintf(state->ideas[state->count], IDEA_LEN,
                 "Core %d idea #%d", e_get_coreid(), i);
        state->count++;
    }

    return 0;
}