Extra Credit Assignment 2

Fuzzing with libfuzzer can be faster and more effective than fuzzing with plain AFL. However, using libfuzzer takes a bit more setup than AFL, since you need to write a libfuzzer target that invokes the API you want to test, rather than just providing a file as input.

In this extra credit assignment, you will get more experience with libFuzzer.
Instructions

Take the giftcardreader.c you used in Homework 1 and add a libfuzzer target for it.

Recall that to use libfuzzer, you need to create a new function:

int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
    // code that calls your API here
}

For more details, see the libfuzzer documentation.

One tricky piece is that the gift_card_reader function currently takes a FILE * as input, rather than a buffer. In addition, libfuzzer assumes that the code you want to test can be compiled as a separate module (with no main function) and then linked with your fuzzer target.

To solve the first problem, you will have to rewrite gift_card_reader slightly so that it operates on a buffer rather than calling fread repeatedly. To retain compatibility with the original API, you could write a wrapper function that reads in the file data and then calls your modified function like this:

struct this_gift_card *gift_card_reader(FILE *input_fd) {
{
    uint8_t *buf;
    fseek(fp, 0, SEEK_END);
    long fsize = ftell(fp);
    rewind(fp);
    buf = malloc(fsize);
    fread(buf, 1, fsize, fp);
    return gift_card_reader_buf(buf, fsize);
}

For second problem, you can just move main() into its own file.

Finally, you should add a target to your Makefile to build the libfuzzer target. I recommend something like this:

fuzzer: giftcardreader.c fuzzer.c 
        clang -g -fsanitize=address,fuzzer giftcardreader.c fuzzer.c -o fuzzer

When you run fuzzer, you will get output like this:

$ ./fuzzer
INFO: Seed: 3916993652
INFO: Loaded 1 modules   (56 inline 8-bit counters): 56 [0x74e230, 0x74e268), 
INFO: Loaded 1 PC tables (56 PCs): 56 [0x52ed00,0x52f080), 
INFO: -max_len is not provided; libFuzzer will not generate inputs larger than 4096 bytes
INFO: A corpus is not provided, starting from an empty corpus
#2      INITED cov: 16 ft: 17 corp: 1/1b exec/s: 0 rss: 37Mb
        NEW_FUNC[0/3]: 0x512f40 in /home/moyix/git/appsec_hw1/giftcardreader.c:12
        NEW_FUNC[1/3]: 0x5131b0 in gift_card_reader /home/moyix/git/appsec_hw1/giftcardreader.c:24
#3      NEW    cov: 31 ft: 32 corp: 2/2b exec/s: 0 rss: 38Mb L: 1/1 MS: 1 ChangeByte-
#4      NEW    cov: 31 ft: 34 corp: 3/4b exec/s: 0 rss: 38Mb L: 2/2 MS: 1 CopyPart-
#6      NEW    cov: 32 ft: 35 corp: 4/6b exec/s: 0 rss: 38Mb L: 2/2 MS: 2 ShuffleBytes-ChangeByte-
#7      NEW    cov: 33 ft: 39 corp: 5/63b exec/s: 0 rss: 38Mb L: 57/57 MS: 1 InsertRepeatedBytes-
#12     NEW    cov: 34 ft: 44 corp: 6/4159b exec/s: 0 rss: 38Mb L: 4096/4096 MS: 5 InsertByte-CopyPart-CopyPart-ShuffleBytes-CrossOver-
[...]

Run your new fuzzer on the gift card reader and fix any bugs it finds. This part is complete when you can run your fuzzer for 1 hour without encountering any crashes.

Additional notes:

    There are lots and lots of memory errors in the current giftcardreader. Address Sanitizer (which is turned on by default) should find most of them and point out where the problem is.

    libfuzzer stops as soon as it encounters a bug, so you will have to fix each bug it finds before continuing.

    libfuzzer will treat memory leaks as errors by default. You can turn this off, but you may encounter problems with running out of memory if you do, so it's better to just fix the leaks.

What to Submit

Submit your modified giftcardreader.c,fuzzer.c, and Makefile.
