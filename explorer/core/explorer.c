/*
 * Parallel Explorer Core - v0.5
 * Supports both Parallel Exploration and Light Chatbot modes.
 */

#include <stdio.h>
#include <string.h>
#include "e_lib.h"
#include "shared_mem.h"
#include "mode.h"

volatile explorer_output_t *output = (volatile explorer_output_t *)EXPLORER_OUTPUT_BASE;

engine_mode_t current_mode = MODE_PARALLEL_EXPLORATION;

const char* get_mode_prefix(void) {
    if (current_mode == MODE_LIGHT_CHATBOT) {
        return "Casual check-in: ";
    }

    // Parallel exploration roles
    int core = e_get_coreid();
    switch (core % 4) {
        case 0: return "Creative: ";
        case 1: return "Technical: ";
        case 2: return "Risk: ";
        case 3: return "Connection: ";
        default: return "Idea: ";
    }
}

int main(void) {
    int core = e_get_coreid();
    output[core].core_id = core;
    output[core].count = 4;

    for (int i = 0; i < 4; i++) {
        snprintf((char *)output[core].results[i], 128,
                 "%s variation %d", get_mode_prefix(), i);
        output[core].scores[i] = 0.5f + ((float)i * 0.08f);
    }

    return 0;
}