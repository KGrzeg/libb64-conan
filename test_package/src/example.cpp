#include <iostream>


#include <encode.h>
#include <decode.h>


int main() {
    const char str[] = "Hello world!";
    const unsigned len = sizeof(str);
    char out[len*2], rev[len*2];

    // base64_encodestate E;
    // base64_init_encodestate(&E);
    // base64_decodestate D;
    // base64_init_decodestate(&D);

    base64::encoder E;
    base64::decoder D;

    const unsigned out_len = E.encode(str, len, out);
    D.decode(out, out_len, rev);

    // const unsigned out_len = base64_encode_block(str, len, out, &E);
    // base64_decode_block(out, out_len, rev, &D);

    std::cout << "input:    " << str << std::endl;
    std::cout << "base64:   " << out << std::endl;
    std::cout << "reversed: " << rev << std::endl;

    return 0;
}
