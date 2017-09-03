CODECS = {
    # miscellaneous
    # disabling bin because its prefix collides with base2
    # 'bin':                  {'prefix': 0x55, },

    # bases encodings
    'base1':                {'prefix': 0x01, },
    'base2':                {'prefix': 0x55, },
    'base8':                {'prefix': 0x07, },
    'base10':               {'prefix': 0x09, },

    # serialization formats
    'cbor':                 {'prefix': 0x51, },
    'protobuf':             {'prefix': 0x50, },
    'rlp':                  {'prefix': 0x60, },
    'bencode':              {'prefix': 0x63, },

    # multiformats
    'multicodec':           {'prefix': 0x30, },
    'multihash':            {'prefix': 0x31, },
    'multiaddr':            {'prefix': 0x32, },
    'multibase':            {'prefix': 0x33, },

    # multihashes
    'sha1':                 {'prefix': 0x11, },
    'sha2-256':             {'prefix': 0x12, },
    'sha2-512':             {'prefix': 0x13, },
    'dbl-sha2-256':         {'prefix': 0x56, },
    'sha3-224':             {'prefix': 0x17, },
    'sha3-256':             {'prefix': 0x16, },
    'sha3-384':             {'prefix': 0x15, },
    'sha3-512':             {'prefix': 0x14, },
    'shake-128':            {'prefix': 0x18, },
    'shake-256':            {'prefix': 0x19, },
    'keccak-224':           {'prefix': 0x1A, },
    'keccak-256':           {'prefix': 0x1B, },
    'keccak-384':           {'prefix': 0x1C, },
    'keccak-512':           {'prefix': 0x1D, },
    'murmur3':              {'prefix': 0x22, },
    'blake2b-8':            {'prefix': 0xb201, },
    'blake2b-16':           {'prefix': 0xb202, },
    'blake2b-24':           {'prefix': 0xb203, },
    'blake2b-32':           {'prefix': 0xb204, },
    'blake2b-40':           {'prefix': 0xb205, },
    'blake2b-48':           {'prefix': 0xb206, },
    'blake2b-56':           {'prefix': 0xb207, },
    'blake2b-64':           {'prefix': 0xb208, },
    'blake2b-72':           {'prefix': 0xb209, },
    'blake2b-80':           {'prefix': 0xb20a, },
    'blake2b-88':           {'prefix': 0xb20b, },
    'blake2b-96':           {'prefix': 0xb20c, },
    'blake2b-104':          {'prefix': 0xb20d, },
    'blake2b-112':          {'prefix': 0xb20e, },
    'blake2b-120':          {'prefix': 0xb20f, },
    'blake2b-128':          {'prefix': 0xb210, },
    'blake2b-136':          {'prefix': 0xb211, },
    'blake2b-144':          {'prefix': 0xb212, },
    'blake2b-152':          {'prefix': 0xb213, },
    'blake2b-160':          {'prefix': 0xb214, },
    'blake2b-168':          {'prefix': 0xb215, },
    'blake2b-176':          {'prefix': 0xb216, },
    'blake2b-184':          {'prefix': 0xb217, },
    'blake2b-192':          {'prefix': 0xb218, },
    'blake2b-200':          {'prefix': 0xb219, },
    'blake2b-208':          {'prefix': 0xb21a, },
    'blake2b-216':          {'prefix': 0xb21b, },
    'blake2b-224':          {'prefix': 0xb21c, },
    'blake2b-232':          {'prefix': 0xb21d, },
    'blake2b-240':          {'prefix': 0xb21e, },
    'blake2b-248':          {'prefix': 0xb21f, },
    'blake2b-256':          {'prefix': 0xb220, },
    'blake2b-264':          {'prefix': 0xb221, },
    'blake2b-272':          {'prefix': 0xb222, },
    'blake2b-280':          {'prefix': 0xb223, },
    'blake2b-288':          {'prefix': 0xb224, },
    'blake2b-296':          {'prefix': 0xb225, },
    'blake2b-304':          {'prefix': 0xb226, },
    'blake2b-312':          {'prefix': 0xb227, },
    'blake2b-320':          {'prefix': 0xb228, },
    'blake2b-328':          {'prefix': 0xb229, },
    'blake2b-336':          {'prefix': 0xb22a, },
    'blake2b-344':          {'prefix': 0xb22b, },
    'blake2b-352':          {'prefix': 0xb22c, },
    'blake2b-360':          {'prefix': 0xb22d, },
    'blake2b-368':          {'prefix': 0xb22e, },
    'blake2b-376':          {'prefix': 0xb22f, },
    'blake2b-384':          {'prefix': 0xb230, },
    'blake2b-392':          {'prefix': 0xb231, },
    'blake2b-400':          {'prefix': 0xb232, },
    'blake2b-408':          {'prefix': 0xb233, },
    'blake2b-416':          {'prefix': 0xb234, },
    'blake2b-424':          {'prefix': 0xb235, },
    'blake2b-432':          {'prefix': 0xb236, },
    'blake2b-440':          {'prefix': 0xb237, },
    'blake2b-448':          {'prefix': 0xb238, },
    'blake2b-456':          {'prefix': 0xb239, },
    'blake2b-464':          {'prefix': 0xb23a, },
    'blake2b-472':          {'prefix': 0xb23b, },
    'blake2b-480':          {'prefix': 0xb23c, },
    'blake2b-488':          {'prefix': 0xb23d, },
    'blake2b-496':          {'prefix': 0xb23e, },
    'blake2b-504':          {'prefix': 0xb23f, },
    'blake2b-512':          {'prefix': 0xb240, },
    'blake2s-8':            {'prefix': 0xb241, },
    'blake2s-16':           {'prefix': 0xb242, },
    'blake2s-24':           {'prefix': 0xb243, },
    'blake2s-32':           {'prefix': 0xb244, },
    'blake2s-40':           {'prefix': 0xb245, },
    'blake2s-48':           {'prefix': 0xb246, },
    'blake2s-56':           {'prefix': 0xb247, },
    'blake2s-64':           {'prefix': 0xb248, },
    'blake2s-72':           {'prefix': 0xb249, },
    'blake2s-80':           {'prefix': 0xb24a, },
    'blake2s-88':           {'prefix': 0xb24b, },
    'blake2s-96':           {'prefix': 0xb24c, },
    'blake2s-104':          {'prefix': 0xb24d, },
    'blake2s-112':          {'prefix': 0xb24e, },
    'blake2s-120':          {'prefix': 0xb24f, },
    'blake2s-128':          {'prefix': 0xb250, },
    'blake2s-136':          {'prefix': 0xb251, },
    'blake2s-144':          {'prefix': 0xb252, },
    'blake2s-152':          {'prefix': 0xb253, },
    'blake2s-160':          {'prefix': 0xb254, },
    'blake2s-168':          {'prefix': 0xb255, },
    'blake2s-176':          {'prefix': 0xb256, },
    'blake2s-184':          {'prefix': 0xb257, },
    'blake2s-192':          {'prefix': 0xb258, },
    'blake2s-200':          {'prefix': 0xb259, },
    'blake2s-208':          {'prefix': 0xb25a, },
    'blake2s-216':          {'prefix': 0xb25b, },
    'blake2s-224':          {'prefix': 0xb25c, },
    'blake2s-232':          {'prefix': 0xb25d, },
    'blake2s-240':          {'prefix': 0xb25e, },
    'blake2s-248':          {'prefix': 0xb25f, },
    'blake2s-256':          {'prefix': 0xb260, },

    # multiaddrs
    'ip4':                  {'prefix': 0x04, },
    'ip6':                  {'prefix': 0x29, },
    'tcp':                  {'prefix': 0x06, },
    'udp':                  {'prefix': 0x0111, },
    'dccp':                 {'prefix': 0x21, },
    'sctp':                 {'prefix': 0x84, },
    'udt':                  {'prefix': 0x012D, },
    'utp':                  {'prefix': 0x012E, },
    'ipfs':                 {'prefix': 0x01A5, },
    'http':                 {'prefix': 0x01E0, },
    'https':                {'prefix': 0x01BB, },
    'quic':                 {'prefix': 0x01CC, },
    'ws':                   {'prefix': 0x01DD, },
    'onion':                {'prefix': 0x01BC, },
    'p2p-circuit':          {'prefix': 0x0122, },

    # IPLD formats
    'dag-pb':               {'prefix': 0x70, },
    'dag-cbor':             {'prefix': 0x71, },

    'git-raw':              {'prefix': 0x78, },

    'eth-block':            {'prefix': 0x90, },
    'eth-block-list':       {'prefix': 0x91, },
    'eth-tx-trie':          {'prefix': 0x92, },
    'eth-tx':               {'prefix': 0x93, },
    'eth-tx-receipt-trie':  {'prefix': 0x94, },
    'eth-tx-receipt':       {'prefix': 0x95, },
    'eth-state-trie':       {'prefix': 0x96, },
    'eth-account-snapshot': {'prefix': 0x97, },
    'eth-storage-trie':     {'prefix': 0x98, },

    'bitcoin-block':        {'prefix': 0xb0, },
    'bitcoin-tx':           {'prefix': 0xb1, },

    'zcash-block':          {'prefix': 0xc0, },
    'zcash-tx':             {'prefix': 0xc1, },

    'stellar-block':        {'prefix': 0xd0, },
    'stellar-tx':           {'prefix': 0xd1, },

    'torrent-info':         {'prefix': 0x7b, },
    'torrent-file':         {'prefix': 0x7c, },
    'ed25519-pub':          {'prefix': 0xed, },
}

NAME_TABLE = {name: value['prefix'] for name, value in CODECS.items()}
CODE_TABLE = {value['prefix']: name for name, value in CODECS.items()}
