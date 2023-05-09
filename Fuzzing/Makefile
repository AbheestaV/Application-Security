default: fuzzer

giftcardreader: giftcardreader.c giftcard.h
	gcc -o giftcardreader giftcardreader.c giftcardreader_main.c

fuzzer: giftcardreader.c fuzzer.c 
	clang-12 -g -fsanitize=address,fuzzer giftcardreader.c fuzzer.c -o fuzzer
		
asan: giftcardreader.c giftcard.h
	gcc -fsanitize=address -g -o giftcardreader giftcardreader.c

test: giftcardreader
	./giftcardreader 1 examplefile.gft

# .PHONY tells make to always assume this target needs
# to be rebuilt
.PHONY: clean
clean:
	rm -f *.o giftcardreader
