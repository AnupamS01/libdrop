class Runner:
    def __init__(self, ip: str, pubkey: bytes, privkey: bytes):
        self.ip = ip
        self.pubkey = pubkey
        self.privkey = privkey


# fmt: off
RUNNERS = {
    "ren": Runner(
        ip = "172.20.0.5",
        pubkey = bytes([0xb3, 0x99, 0xd3, 0x0f, 0x6b, 0x64, 0x3e, 0xa3, 0x06, 0xbc, 0x8a, 0x67, 0x98, 0x3f, 0x09, 0xf3, 0x23, 0x83, 0xab, 0x67, 0x44, 0xa1, 0xd1, 0x55, 0x97, 0xc4, 0x8a, 0x0d, 0xbb, 0xae, 0x8f, 0x58]),
        privkey = bytes([0xe9, 0x13, 0x19, 0x8d, 0x8b, 0xeb, 0xc4, 0x8d, 0x23, 0xd7, 0xec, 0xcb, 0x80, 0xc2, 0x37, 0xf5, 0x98, 0x29, 0x35, 0x8e, 0x17, 0x00, 0xa5, 0x45, 0xd4, 0xdb, 0xba, 0xe6, 0xb3, 0xa0, 0xa9, 0xc9]),
    ),
    "stimpy": Runner(
        ip = "172.20.0.15",
        pubkey = bytes([0xfb, 0xb3, 0x25, 0x11, 0xc4, 0x5f, 0x3b, 0xb2, 0xf8, 0xdd, 0x67, 0xc3, 0x22, 0xd4, 0x7e, 0xd6, 0x23, 0xf1, 0xaa, 0x94, 0x2e, 0xc1, 0x75, 0x8d, 0x6e, 0x66, 0x99, 0x47, 0x1b, 0x98, 0x33, 0x42]),
        privkey = bytes([0x74, 0x70, 0x14, 0x96, 0x38, 0x06, 0xf7, 0xd8, 0xfe, 0xcb, 0x32, 0xac, 0x45, 0xeb, 0x9a, 0x91, 0xdd, 0x75, 0x70, 0xd0, 0xd5, 0xfb, 0xb4, 0x20, 0x2f, 0xb4, 0x85, 0x9f, 0x84, 0x63, 0xe3, 0x98]),
    ),
    "george": Runner(
        ip = "172.20.0.25",
        pubkey = bytes([0x47, 0xb1, 0x09, 0x12, 0xc0, 0xcc, 0x8a, 0x62, 0xf8, 0x20, 0xfc, 0xe0, 0xba, 0x5b, 0xb9, 0xc4, 0x1c, 0xfc, 0x5d, 0x86, 0xe7, 0xe7, 0x95, 0xc9, 0x8d, 0xd8, 0x53, 0xe1, 0x33, 0x12, 0x2c, 0x5b]),
        privkey = bytes([0x16, 0x7a, 0x91, 0x83, 0x14, 0xd6, 0xf9, 0x21, 0x45, 0xec, 0x7b, 0x3d, 0x26, 0x57, 0xa8, 0x6f, 0x2a, 0x23, 0xfe, 0x61, 0x25, 0x92, 0x33, 0x09, 0xb9, 0xa2, 0xfe, 0x9d, 0xda, 0x52, 0x8e, 0xc7]),
    ),
}
# fmt: on


class TestFile:
    def __init__(self, size: int, id: str):
        # in kilobytes
        self.size = size
        self.id = id


FILES = {
    "thisisaverylongfilenameusingonlylowercaselettersandnumbersanditcontainshugestringofnumbers01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234561234567891234567891234567890123456789012345678901234567890123456.txt": TestFile(
        size=1 * 1024, id="p3cYEJWds51Uqb174hrbHxfE6ASz_ioErmh39jLsiWU"
    ),
    "testfile-small": TestFile(
        size=1 * 1024, id="BzgNijPq2HAy4UH75K3kqXou9sTVT7AbSWRGUrU7oGI"
    ),
    "testfile-big": TestFile(
        size=10 * 1024, id="ESDW8PFTBoD8UYaqxMSWp6FBCZN3SKnhyHFqlhrdMzU"
    ),
    "deep/path/file1.ext1": TestFile(
        size=1 * 1024, id="CKVHseb1gM6DuUGwQU9D25GTTyehos44Si282V5Ut_E"
    ),
    "deep/path/file2.ext2": TestFile(
        size=1 * 1024, id="AP62vXu2WAmIOwxYUs_oL7U_YjeOe8ixrhNKKuAwHNs"
    ),
    "deep/another-path/file3.ext3": TestFile(
        size=1 * 1024, id="mTtUD_megD0_UiyhRmVjYefqycu1lkG9hH62e646Llw"
    ),
    "deep/another-path/file4.ext4": TestFile(
        size=1 * 1024, id="FFiT0wxJnodvDGZNYAX_jUojoYLKLpeIccyWQBzapfE"
    ),
    "testfile-bulk-01": TestFile(
        size=10 * 1024, id="cO4I0umdTfN9bZvQoYI-7z3XvJUcA4b2Atw8CFDOHjg"
    ),
    "testfile-bulk-02": TestFile(
        size=10 * 1024, id="4-Dt2b89ubTwW8GF0-n1wJo5Iq-Zj74d4pBiKaD7t3s"
    ),
    "testfile-bulk-03": TestFile(
        size=10 * 1024, id="DOmO7NCdwBNb5ES6KnLt_s4KuLW6tGDYDhIbTZEgaao"
    ),
    "testfile-bulk-04": TestFile(
        size=10 * 1024, id="ZqICxNTPq3Mss9lE1KWARaP-2myx2-aNR7LtYmJmCD0"
    ),
    "testfile-bulk-05": TestFile(
        size=10 * 1024, id="TZ8p7dXbUhvbB3oMQj_5rQes6Hn_kBBiSsD_v_y5cCg"
    ),
    "testfile-bulk-06": TestFile(
        size=10 * 1024, id="TDcRO-4urGbJsmsCAdoAtTQQjvcXWKD8IDm9J_qg0i4"
    ),
    "testfile-bulk-07": TestFile(
        size=10 * 1024, id="21vkb4qcrSRmN49QZuN_8A-Yzexfqtm7_m2RNEVkyMU"
    ),
    "testfile-bulk-08": TestFile(
        size=10 * 1024, id="0wjysbL9CZu6qGJEddKozpCsVsK2f_W7xQLi4dUrCFg"
    ),
    "testfile-bulk-09": TestFile(
        size=10 * 1024, id="yqHoVs1jXFdsJBfHOMdjR63NVt4tXvigLn7bMWXNKa0"
    ),
    "testfile-bulk-10": TestFile(
        size=10 * 1024, id="0rHKOnFZFo6kNnwkDfaMDE8luAqfFWqUJjtdB7IIqVA"
    ),
    "nested/big/testfile-01": TestFile(
        size=10 * 1024, id="KKzrrYLyKL54hNit9g748Q2TMi4hLA-pPeoqspNlBOA"
    ),
    "nested/big/testfile-02": TestFile(
        size=10 * 1024, id="7uo62xhQBZK-6z-ndyFzRCPpzWPO2sJTgnu5D2t1Zbw"
    ),
    "testfile.small.with.complicated.extension": TestFile(
        size=1 * 1024, id="tHK8wmpZjD1mtQeIzigO7qZfRemEk4oSQu0IocoiCmE"
    ),
    "with-illegal-char-\x0A-": TestFile(
        size=1 * 1024, id="a8vdPYj-41hoFD2OCJqrf4x9SZuqibscR9XPUPijTuY"
    ),
    "duplicate/testfile-small": TestFile(
        size=1 * 1024, id="IY3xuWiT4zBQ3tyxKvmBHoikxfRvyFPfHTNNPIMQoL4"
    ),
    "duplicate/testfile.small.with.complicated.extension": TestFile(
        size=1 * 1024, id="9CvPHrjnPOQa_2Y-x2yUBESKcTmbj-RdYEs3VKww5Ys"
    ),
    "zero-sized-file": TestFile(
        size=0, id="d5d4ohM4nRb8b6-Ob19WnSAr_uTtGoUXjT-L575CCMY"
    ),
    "duplicate/testfile-big": TestFile(
        size=20 * 1024, id="Jr2sHMHPjPP5Y19bGJMf17GeT3B4Jrs1ozB1UnFcRzo"
    ),
}
