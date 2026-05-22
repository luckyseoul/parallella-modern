/*
 * Shared Memory Helpers for Epiphany ↔ ARM Communication
 */

#ifndef SHARED_MEM_H
#define SHARED_MEM_H

#include <stdint.h>

#define EXPLORER_OUTPUT_BASE  0x8f000000
#define MAX_EXPLORERS         16
#define MAX_RESULTS_PER_CORE  16
#define RESULT_LEN            128

typedef struct {
    uint32_t core_id;
    uint32_t count;
    char     results[MAX_RESULTS_PER_CORE][RESULT_LEN];
    float    scores[MAX_RESULTS_PER_CORE];
} explorer_output_t;

#endif // SHARED_MEM_H