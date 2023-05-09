#include "giftcard.h"
#include <stdint.h>
#include <stdio.h>
#include <strings.h>

int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size)
    {
        // code that calls your API here
        gift_card_reader_buf(Data, Size);
        return 0;
    }
