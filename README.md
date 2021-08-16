# Thessis Ecommerce

## Installing

### Step 1
Run the venv
```
pip install pipenv
pipenv shell
```

### Step 2
Install th requirments
```
pip install -r requirements.txt
```

### Step 3
Create SQLite databse, run migrations
```
cd store
python manage.py migrate

```
### Step 4
Run Django dev server
```
python manage.py runserver

```
## Stracture
Tree Stracture
```


```





```
ThessisEcommerce
├─ .DS_Store
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ master
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ master
│  ├─ objects
│  │  ├─ 00
│  │  │  ├─ 2136f25d703aa05b42378b427b35089af18bbb
│  │  │  └─ 49577ff42e1c18e8c4ab55b3629036d7ac4c8e
│  │  ├─ 01
│  │  │  └─ 9814924645f377fddaa3a8ec1244d82c30be08
│  │  ├─ 05
│  │  │  ├─ 34e53bb510b82ec20ec52d3c45e7b81b388c06
│  │  │  └─ d8e75d679aeb135d41340ba032f6586c3f054d
│  │  ├─ 06
│  │  │  └─ 2fa110f36c0c33ad37bf625b43fd716ad62aec
│  │  ├─ 08
│  │  │  └─ 5f43e88574156d690da5c943cbb2c1c4120ed1
│  │  ├─ 0a
│  │  │  ├─ 73b577642d789f7ffa8c5a9220bce53822921a
│  │  │  ├─ b57ef24a02f1e9988b2478ab5c994411175b7c
│  │  │  └─ d2317e4ef76ec68e01ef606a11c65d069d63e5
│  │  ├─ 0b
│  │  │  └─ 4aea7d720a22cd49a64875a0b3bee587a5f2c2
│  │  ├─ 0c
│  │  │  └─ 0e8ead4d513cddee6c8af7e828bac5b6910988
│  │  ├─ 0d
│  │  │  ├─ 46680b61f51acb462505fff24c3d5414219e12
│  │  │  └─ 9fa3171e1a6fb0cc5072446dda804f3f8f3a3e
│  │  ├─ 10
│  │  │  ├─ 2d3478f2e5a77f832fc8c3e45abda998216634
│  │  │  └─ e8242d793e72a54ab507104e7ff43dfe0ed2d9
│  │  ├─ 11
│  │  │  └─ c3b59f702ecf6f0044b511159c5df006075b66
│  │  ├─ 14
│  │  │  └─ b613f58d7500926dfd42f907bea3eac1ceb6b1
│  │  ├─ 15
│  │  │  ├─ 592853c0d64135cba980e2c564bbee31e881d4
│  │  │  └─ af5bc8e2c97acd53ab80623efc9c742b236556
│  │  ├─ 16
│  │  │  └─ e72c9a202f780a2d19a3dd7ea1b96b7d1f1785
│  │  ├─ 17
│  │  │  └─ 538bf12cb35b6d964dcdc1e379043190b536cf
│  │  ├─ 18
│  │  │  └─ 4dc1a73937283ef585e6f9e7ce1c172899022a
│  │  ├─ 19
│  │  │  ├─ 0fd48172599159aacd422ab1a772e8e0e15eb1
│  │  │  ├─ 2152d0c53d0af5f3aedd0c3acbf1290b126480
│  │  │  └─ c55130e7b76150b2e5845719f9351e5af0dcb5
│  │  ├─ 1b
│  │  │  └─ 2f51b86a05793829cf4989e84f3e8dbf42fce6
│  │  ├─ 1e
│  │  │  └─ 63a4d4e0b282e42839a18880c52e47c78629a4
│  │  ├─ 1f
│  │  │  └─ c0645242756376caa359edd57fc1fe6a3a2255
│  │  ├─ 20
│  │  │  └─ 504b8c500e08a5ed22ed2b4102d822ae4a77c6
│  │  ├─ 21
│  │  │  └─ e8a147108e6e932448d64e11452e9bafd550f6
│  │  ├─ 22
│  │  │  ├─ 3d3069389c5108a2c859017fbb68ed0769e535
│  │  │  ├─ 4eab4e346e7e191ecff2814fbf71dbf7bc3bb1
│  │  │  ├─ 84d4ce38a1707022b50a5140532045978fe552
│  │  │  └─ 973df6ffa5cfeb4bbb6deb06a7d45110b59a1f
│  │  ├─ 23
│  │  │  └─ 5463c8713ba5e0e15d0f20bb2b453676272a90
│  │  ├─ 25
│  │  │  ├─ 11ab30b39799d8ada38e56d3fd8ccff20cb164
│  │  │  └─ 2bc9758234ef5dd8051a3607c3fc040c10c9bc
│  │  ├─ 26
│  │  │  └─ 6a076319cdcf7ecaeb3bfccd58b7abaae23ff5
│  │  ├─ 28
│  │  │  └─ 920dd555844f90aefd8722c7f22fad720c8d2f
│  │  ├─ 2a
│  │  │  └─ 6cb65465a494da3acf77f78bdb395e814e741e
│  │  ├─ 2b
│  │  │  ├─ 0af0d2127c6e1ec50474eefda69541387ca5b3
│  │  │  └─ 25cf6bed7f5cf9fdb3278962684613bf2d56a6
│  │  ├─ 2c
│  │  │  ├─ 25b05c6a99a1d81aef1d607cb2612ec025f428
│  │  │  └─ 7f35e144d8d82deb59250740b3f32aa812654b
│  │  ├─ 2d
│  │  │  └─ 17caf3ac73566b8e651614457532e28e7cf5c4
│  │  ├─ 2e
│  │  │  ├─ 3e0ad2fc31ef0db930d3af5eda4e1aaada83d2
│  │  │  ├─ 88da977f0bd11727f6ccf286e1b3616aefb003
│  │  │  ├─ a74c824e7c5867bb7ce2e819de271fc536b87b
│  │  │  └─ c474098255c5be410e6b75a05245e670abf83b
│  │  ├─ 2f
│  │  │  ├─ c37d8848134e5b0d314e83c85b4a7365749bf9
│  │  │  └─ d107dd61defae9e726545db8865da203437756
│  │  ├─ 30
│  │  │  ├─ 02d4339b8661c277835918845b7ed61f695370
│  │  │  └─ 1732b46227e051c5c9baa260d5b75460739f31
│  │  ├─ 31
│  │  │  ├─ 2e09eb0d148bc478daf3de6c8efec28ad39538
│  │  │  └─ c80005cadfcc7e14ef874be5a00b126890c8de
│  │  ├─ 33
│  │  │  ├─ 1307466af50a3b471f68e4204d664a5a571788
│  │  │  ├─ 83e4e0fa48a846289afc487fa1037e31596e40
│  │  │  └─ cc640931a81e6df0befdfbb016cbd836225340
│  │  ├─ 34
│  │  │  └─ ce2a5fc5ad6105b171b6fc064a76e1dc952338
│  │  ├─ 36
│  │  │  ├─ 24ee1c5598a2d9ff9d3e7388874210310fd01e
│  │  │  ├─ be345a1854ee0687424cd1d5d7ab080313f2db
│  │  │  ├─ cb4019a22c9409fc1fb7d4215ac00dd6cf4baf
│  │  │  └─ dc4ca97700bf3d90defaa5d7afa928fc4a4621
│  │  ├─ 37
│  │  │  └─ 487fadcadd5e71d4538b45ff4cc34efc921424
│  │  ├─ 38
│  │  │  ├─ 333220c6e31dd8ce6ef6b011acda0effc63b46
│  │  │  ├─ 465e5ae301b3ddefabfe22b188c4fee52182c0
│  │  │  └─ a54c7c9f1baaeee51b0c5ea8b0d1d814bed7ea
│  │  ├─ 39
│  │  │  ├─ 3a2f91bdd0287da950c56716c6a41f8f268e99
│  │  │  └─ 8fad0c9340b34fd7f94f0c55483bfdefb8ef6b
│  │  ├─ 3b
│  │  │  └─ 5691f46838da2b97611eab110872c60f77eb2d
│  │  ├─ 3c
│  │  │  └─ 92f07ccd5d758a60b91f3839105b13a6fea9f0
│  │  ├─ 3d
│  │  │  ├─ 6065017eebfbbd86fc08dbbda3b63d737c8d2a
│  │  │  └─ 6afb4c3405b63fe3c9d2419c73a95e7237ae23
│  │  ├─ 3e
│  │  │  └─ 7442f33b143aa81e13526fed7ee224cb56232d
│  │  ├─ 40
│  │  │  ├─ 26e09d43ffe0ebd925a32b523577b1bc7cc909
│  │  │  ├─ 91891c371e455b869ba33b0c970dd6e8e8ac5b
│  │  │  └─ f7141cee1b86c6bc874c01f15c1ad2bc3d3692
│  │  ├─ 41
│  │  │  └─ 658c1eba55e7bed44c1fa8928b3d98bffa3ff9
│  │  ├─ 42
│  │  │  └─ 7de1c6abe901274d41e68278e8dc8b9ef49b52
│  │  ├─ 43
│  │  │  └─ 9447da0bdda6509f8df3f3578439d9e97de96b
│  │  ├─ 47
│  │  │  ├─ abcbfd937da932ff970d20733e7125fed1defb
│  │  │  └─ c644e5942558d86a3cae3b751f611ef26f7f65
│  │  ├─ 48
│  │  │  └─ 713e5bc60e69693317639cab1b78733d77b1eb
│  │  ├─ 49
│  │  │  ├─ 1b97dd8fc15e308704557eed30c96bfaf099a4
│  │  │  └─ 310b5e5805cb8e311aa347fa8dc714c9ae5db2
│  │  ├─ 4b
│  │  │  └─ 43b73e5074c3c9090a03b82919621ea6803881
│  │  ├─ 4c
│  │  │  ├─ 2f1300f9e075b6639719d507fec794e2024c90
│  │  │  └─ 7c0790f22ce2bba03403f59470f714de9c1849
│  │  ├─ 4e
│  │  │  └─ d815400fdea5da340594da7deeb7a4ccf7c38f
│  │  ├─ 4f
│  │  │  └─ ea2a9c8242752e91492dfa428d4653ec0e8e44
│  │  ├─ 50
│  │  │  └─ 08ddfcf53c02e82d7eee2e57c38e5672ef89f6
│  │  ├─ 51
│  │  │  ├─ 5aa723553ee1b68b073ccd899cfb1db84a3fcd
│  │  │  └─ e8a79c239d836655cf3a87ac445e32460e5fb3
│  │  ├─ 53
│  │  │  ├─ 4dfc1a2225f5cd991c1e5e72c924198f5e1671
│  │  │  └─ 91a044457ab06b71ac052a05f07db45af18a71
│  │  ├─ 54
│  │  │  ├─ 00d8048fbff1f4d0af3a20e3cae92795cfbba4
│  │  │  ├─ 21ebe7948147df908990f52432b601681ee535
│  │  │  └─ 955eb2c6ac61ef85d1c9d728ab41e0e0d1a850
│  │  ├─ 55
│  │  │  ├─ 2d2fd569060c77d71ec5f98ee61ad238367bfb
│  │  │  └─ a66a8db86ddf0c6c0a88a1ede88ad9e659a475
│  │  ├─ 5a
│  │  │  └─ 8739cd8f35514595b99bd50950827179360a03
│  │  ├─ 5c
│  │  │  └─ fa2ad4a98207c1cd561214b2ca633ee7669e2d
│  │  ├─ 5e
│  │  │  ├─ 05aa8123843992b8634ef15e0ed115ae4ed4fa
│  │  │  └─ 25714d7c3a1e8bb2add5cf1411eb9f522149af
│  │  ├─ 5f
│  │  │  ├─ 3a14e0a5ca6d20cc4fac708979e807b0d51bc3
│  │  │  └─ 5560ba058af0c065311f35088ef0e013916281
│  │  ├─ 61
│  │  │  └─ 2ee4cce867ecabaa08feb05fe62811d8a90bf5
│  │  ├─ 66
│  │  │  └─ b4029bb38d45b32c7d570cb2e3ff3df3d79e02
│  │  ├─ 67
│  │  │  └─ d40f82010e88e132c7a74344928ff6246b2169
│  │  ├─ 68
│  │  │  ├─ 839fecb90c00d1538f74b3973558083215e1f4
│  │  │  ├─ a18d7e45404c2e82b19de832d1c3431e7be211
│  │  │  └─ e42c265d05ca28147aa1732495c84fe245823b
│  │  ├─ 69
│  │  │  └─ bc7f83c28a695469a1b5e62cce1d58584249fd
│  │  ├─ 6b
│  │  │  └─ a365a44fb8104f6379f2ef6cded644b08c123b
│  │  ├─ 6c
│  │  │  └─ 77824a51fb993ed6dbf96f5f387704ecde76fd
│  │  ├─ 6d
│  │  │  └─ 43733cd26a449fce94f802ef961d45c60756b7
│  │  ├─ 6e
│  │  │  ├─ 2107185f0be6489af2e75216080919d5c813c0
│  │  │  ├─ 479db369f2c2f0cf183aa913656cd1b9c0a47d
│  │  │  ├─ cd8815ddaf65e42930a6ee1f0906f5b1919d8b
│  │  │  └─ ef7cae16bc958f44704d51a8f3be69abf2f0a7
│  │  ├─ 6f
│  │  │  ├─ 3a2913e199cebe9ace75cf7e5a2818da27fbd3
│  │  │  └─ 7b58489c6fe76af1597fad93bd8ebe36114eb9
│  │  ├─ 70
│  │  │  └─ d229618fc45c23b6bc757f7c31da6967b5ea79
│  │  ├─ 71
│  │  │  ├─ 258d4a8e6c31d099dc903568e93756d5ab8b65
│  │  │  ├─ 59bb19acdff4b59bd64060972e6371eb3deebc
│  │  │  └─ a836239075aa6e6e4ecb700e9c42c95c022d91
│  │  ├─ 72
│  │  │  └─ 7a7791f1c6d2d469b398f292186b58cc94eaa5
│  │  ├─ 73
│  │  │  ├─ 3165ac4a4135c871d5e5f1f061f9dc9a035e6a
│  │  │  └─ f61a0746a9589f0e153dc1b0256c4cdc3e45e0
│  │  ├─ 74
│  │  │  ├─ 70bdf47227d7e19a70aec43fab0f2fc6c65657
│  │  │  └─ 71cf621566d3db697bb648d407264bd9278a9d
│  │  ├─ 76
│  │  │  └─ 408eefd280a25f168eb1a84a48341bfeac0c36
│  │  ├─ 77
│  │  │  ├─ 6ca0848e0e1cef4a5ea355586963995d7e16fb
│  │  │  └─ bd70c2d783f40ff75e8c64a5726ef0b3dd47b6
│  │  ├─ 79
│  │  │  └─ d5b10e23fe4eedc27c441921b3865b9cff8afc
│  │  ├─ 7a
│  │  │  └─ d85a028338bca9dd1ed3763acbae947a79b0a9
│  │  ├─ 7b
│  │  │  ├─ 1317d0e58fd99cecf89683b3c9389045187710
│  │  │  ├─ 18993aee0df66afe1aeea81180c7a2003a1875
│  │  │  └─ 6f02b189423df89544d06c600dec11398e7225
│  │  ├─ 7c
│  │  │  ├─ 3a965b887e3fad1db7ef0015d10e36feb5d722
│  │  │  ├─ d7930035ea1240b9b34a65a51f30a112d6368c
│  │  │  ├─ e503c2dd97ba78597f6ff6e4393132753573f6
│  │  │  └─ f71ed864dcd6a54b6bef06ab1d74ce679ac3a8
│  │  ├─ 81
│  │  │  ├─ a61692671feaaa5483cab2b60b8bb7c2788665
│  │  │  └─ f89b9dce6d731b7bd94a6810a1d781a8044a1e
│  │  ├─ 83
│  │  │  ├─ 1a00a6371d0b332e9eb8b736c2bf898f0a7a9e
│  │  │  └─ e7c33ddd8376027948d097c9393656447ee141
│  │  ├─ 86
│  │  │  ├─ 4018a37213732957b487874e806a3d1aa55b62
│  │  │  └─ eb67927543ccc9134d0a84899c4c8ee72f82f2
│  │  ├─ 87
│  │  │  ├─ abbde1a355bfbdd0591b994715cd1fe2156a4f
│  │  │  └─ e69f5fa12434f889539443667325e9e5fc058a
│  │  ├─ 88
│  │  │  └─ 6485fdf8d01895a7a765e4dee07278d50d9288
│  │  ├─ 89
│  │  │  ├─ 04fbd71ca01ceaa22b672bd2d6a5c43cb698f7
│  │  │  ├─ 27113ffa50e696785235e776537e813448cc03
│  │  │  └─ 9b9708cfb1ed405c455fa22ba8263866ee9c77
│  │  ├─ 8b
│  │  │  └─ 3b979191b3606c4f811ebab497149183012dcf
│  │  ├─ 8c
│  │  │  ├─ 38f3f3dad51e4585f3984282c2a4bec5349c1e
│  │  │  ├─ adf318799bcde5135b182fd91f64e4702ee67d
│  │  │  └─ fe69c33129c1ccf8f4796cda8bdeaed807c79e
│  │  ├─ 8d
│  │  │  └─ 71672125a7b0c75ef6800bab6044fbc7b00b52
│  │  ├─ 8e
│  │  │  ├─ 028277af0389e06f67f703ea0a88f5b905f632
│  │  │  ├─ 3b513207f9b7c11afdea33b81911645d23b85f
│  │  │  └─ d4f51f70e802ddbad1495d298a1c4d2fce770f
│  │  ├─ 8f
│  │  │  ├─ 2bd579d39a61275795d04c0dfbf7f83694340e
│  │  │  ├─ 809550ad3ab08fa853d8df4edb2a00883b610e
│  │  │  └─ aec5f51832842fd679020cfba274d0226a9838
│  │  ├─ 90
│  │  │  ├─ 130162705727f548f7eb3f74230fbf2eaec859
│  │  │  ├─ 6c216801784b8fd0e19bd318992d075cb811b8
│  │  │  └─ e2c1f21b30609622f13a673d4c9db7489245f6
│  │  ├─ 91
│  │  │  ├─ 8bce288ad3283985215ba1d7e206536570c852
│  │  │  └─ cf8f661ba7d713a49f3a3cb03d426639eb05e6
│  │  ├─ 92
│  │  │  ├─ 6da8a030ce63dbc744170f7bb0801143e507ca
│  │  │  └─ a3f20a39267ae7f45144f412a995a663730360
│  │  ├─ 93
│  │  │  └─ 8a4ab206e6c8ea2a156622a77e27eda13ea242
│  │  ├─ 94
│  │  │  └─ d0b0ae9c06851a5e1c30c5e83d2cffb728f9e4
│  │  ├─ 95
│  │  │  ├─ 88e1e47bea911c66c3a5e08b45bf32ff6982a1
│  │  │  ├─ 915f2e98476ba7f14ff2f55b79bd9d09a3e677
│  │  │  └─ a68e8c45f342fc5163465df62406e4df37147c
│  │  ├─ 96
│  │  │  ├─ 09eedb10ce789ce9fa0055b163ffd717f1a101
│  │  │  ├─ d7f681a3914b2d385d4e11e352b6ce02f6c66a
│  │  │  └─ e28f07e4eeaee29ae24201dae1e1c8c7552878
│  │  ├─ 97
│  │  │  ├─ 1aa5b092d96c71797f084de94638a596223418
│  │  │  └─ 533c4cc5e798e3cc0d10811faa5046d7ada8d6
│  │  ├─ 98
│  │  │  ├─ 5e6931e53dce7e0b0c6262a2f01e09b502260e
│  │  │  └─ 8937c0ab467cc84aa216ee4ba3bd348e434d68
│  │  ├─ 99
│  │  │  ├─ b8b46df1c9c41e5e8d38c822192cfc1f173de9
│  │  │  └─ dfca729253d7f906433e9cc562bbcdbf1b0ef0
│  │  ├─ 9b
│  │  │  └─ f6f4803417cf1659fc2b4d3ae6dcba24a3c7c9
│  │  ├─ 9d
│  │  │  └─ 1dcfdaf1a6857c5f83dc27019c7600e1ffaff8
│  │  ├─ 9e
│  │  │  └─ b924aadbf3cc6dab3d75f9387482711aaefc2a
│  │  ├─ 9f
│  │  │  └─ b6929eb9dcd6704e079447b506093e6c74418c
│  │  ├─ a0
│  │  │  ├─ c66e0380269281db337bb36d991caac6d5e417
│  │  │  └─ f776fcf05ae4de4679ef8bf2659ffe71e5991c
│  │  ├─ a1
│  │  │  └─ 0cb0910740826d49cff9accd3f55e082821539
│  │  ├─ a3
│  │  │  ├─ 27572bd87156bdf8b2f826d2b6617c07edcb04
│  │  │  ├─ 4234e32e4ee39331a731f7f3ec9e4501cf7dc5
│  │  │  ├─ 8deff6b07c3832ec6b845cd57cdec8fc3adc67
│  │  │  ├─ c0466745a45734d6a9cf6a503ad710f3e2eed7
│  │  │  ├─ cbfd3e70fe6c1568ab8399f93fc6b08751fa27
│  │  │  └─ d89d82ce594341d7e671fdf2311cb8d5d9b3aa
│  │  ├─ a6
│  │  │  └─ c723924b9b9c2f2be0cd002bd321512b1c9bea
│  │  ├─ a8
│  │  │  ├─ 1c8ee121952cf06bfaf9ff9988edd8cded763c
│  │  │  └─ a991be3f079e10820686c597e00b6e0c3c9c53
│  │  ├─ a9
│  │  │  ├─ 59721a5e4958df6e4538716770ac478f2da845
│  │  │  ├─ 68c8a35226353b2d369fc3448bafbcc6fe2f94
│  │  │  └─ 84fe5f5af1bf61fe639227873cd2b9c38cd48e
│  │  ├─ aa
│  │  │  ├─ a5c334a726247b6255fc8405ef9260ac773385
│  │  │  └─ d55ce16527a17f110d9b2983ceac45239331f5
│  │  ├─ ab
│  │  │  └─ 19235026dee0be2adfaf730df1a93860b623ac
│  │  ├─ ac
│  │  │  └─ 456efe843a9f22a34923f037e43a362f86f133
│  │  ├─ ad
│  │  │  └─ ca6cc512302f68074069cd37cca3dee2107ab0
│  │  ├─ ae
│  │  │  ├─ 3209a0457f003743a4d1ae29cb756ffef6692e
│  │  │  └─ 72933d441a5be5143dec84147bef493b82f71f
│  │  ├─ af
│  │  │  └─ e861f33370c2df14f29a3f83047dd1a0f262ee
│  │  ├─ b0
│  │  │  └─ fff7b2e031fb0cfd8fa363800244be04b0fa98
│  │  ├─ b2
│  │  │  └─ 65c10cff762c91555687fbe225fd65c62ca51c
│  │  ├─ b3
│  │  │  └─ 9e365310641917e10d768d795ce4b077809cd8
│  │  ├─ b4
│  │  │  └─ 89c33aaaa63f70d081b6d6ef77c20fc054efad
│  │  ├─ b5
│  │  │  ├─ 8b056fff9c7257c84f5d127e0e5799ee493b04
│  │  │  └─ bf89ce41b7fc6d8235a775cf0f281a14adb50d
│  │  ├─ b7
│  │  │  └─ de22ea271bd51b0f47f8b994b4a0248b039c8d
│  │  ├─ b9
│  │  │  └─ 532228fdec316ab5c1ae4b2da1c734346877cf
│  │  ├─ ba
│  │  │  └─ 69e6a9d0a08da7473b9516fc31801572a45554
│  │  ├─ bc
│  │  │  └─ 8a269c68dafaaf5aaa7920e7a17baff0748360
│  │  ├─ be
│  │  │  └─ 5c1af013077bfcab0f4284610ee4ff35936c26
│  │  ├─ bf
│  │  │  ├─ 6fd790baf4aa440e669f1d722481eef7cd1cf1
│  │  │  ├─ 936db4d3ee18b30473e7f6fc129b0546e3ff8c
│  │  │  └─ 9e12c1b1fed5d0e613a210aa63055419eea1da
│  │  ├─ c1
│  │  │  ├─ 04fbc19c9dc91119474a5f081c7fb42a63b071
│  │  │  ├─ 2f6b4b8d2b429b24f3f5a05c94b84ea9698b08
│  │  │  └─ ead6057b9af40b5c49fe192adb3a8cb82df880
│  │  ├─ c2
│  │  │  ├─ 05e6fd3cae5dbfd991d499c7495c9228a804c3
│  │  │  ├─ 5c925804a03f1217bd23faee172f63549eedf2
│  │  │  └─ dfddf2ab257901aa7745c902d12e123e1f8719
│  │  ├─ c3
│  │  │  ├─ 0976c0f7cac60f1d17b5bb1adfca8ae6979acf
│  │  │  ├─ 93225fd886d1bb7a13b8073295fc2bbd2dc6ca
│  │  │  └─ c6eb8b9d630c89add5a8f2c269bef0962c4224
│  │  ├─ c4
│  │  │  ├─ 5f74b5841d37ad826432e55dab206b6dc41efe
│  │  │  ├─ 8b30f255761dde7920d505544d9bb490d3415d
│  │  │  └─ e4632486d863337c1c73478ddb3c20726c55a0
│  │  ├─ c5
│  │  │  └─ a3e1c4f295e8f751512aa143f73d3cd65b9e02
│  │  ├─ c9
│  │  │  ├─ 3b1651bca6facf942ab34420b43dff7f81c608
│  │  │  ├─ 4ffba218f66c125da4b001daf07e1901d5ea3e
│  │  │  └─ 6bfa54207596bc5ef9e67051c89f18dc3e8b27
│  │  ├─ cb
│  │  │  └─ 1ebc99091540cea8f27c79e71525195f08ec2a
│  │  ├─ cc
│  │  │  └─ 7898b7db7cb7e3479c8f7f3c2e62d44e253ea5
│  │  ├─ cd
│  │  │  └─ 17184480749da6b17be04819f48df4f50b6e29
│  │  ├─ ce
│  │  │  ├─ 2eeefa4456c163753e2e5fb369cc49507598f4
│  │  │  ├─ 4acb7e0a1bba1f1de07fcd698def06cc0ca378
│  │  │  ├─ dc337979f5d3776d68ecbe442e39f53aaddc2d
│  │  │  └─ f90a53ace14dac303310bf7f83d49bdef6685d
│  │  ├─ cf
│  │  │  └─ 0ad06b8e8f4ed819e8b2363a44896c39bef090
│  │  ├─ d0
│  │  │  ├─ 433e644171cf476932740cd8e20b14ba324f56
│  │  │  └─ 7aec867f32fc72037869bfd7e6fa7e2ae4a02c
│  │  ├─ d1
│  │  │  └─ 28566ad0d162bde3453f7fdcd293f6f6773ea2
│  │  ├─ d3
│  │  │  ├─ 6a557ebe37d5870f5fcc5dd09d3506de3f2c9c
│  │  │  └─ 96e315cbe6892620bc7ae2893860eb4f55dd1f
│  │  ├─ d7
│  │  │  └─ dc4e75d0889316ecc93c8de67b9303a2da770a
│  │  ├─ d8
│  │  │  └─ 5e8715b58d5233f11f12750323cb85168f409d
│  │  ├─ d9
│  │  │  └─ 5f3d052f1a17e9e24394425ea0ca649cc730de
│  │  ├─ da
│  │  │  ├─ 2c80748672ed8732133d96a8c12ed38494d26d
│  │  │  ├─ 624193a06e4346f286300d85962bb7fb3d7f3a
│  │  │  └─ fdd58d3200fd597ce8b7660ee7773d4b9bdd35
│  │  ├─ dc
│  │  │  └─ 5b2e1295eb34c1c5b97c5d4391293779f1cf4a
│  │  ├─ dd
│  │  │  └─ dec961908158879c2343c7d4fe2c2d0608cfd8
│  │  ├─ de
│  │  │  ├─ 109c59edaa93eb5dfc47bfb7fad984e6ba9929
│  │  │  └─ 670673e316d9eac3a6c11a22addb9897252425
│  │  ├─ e0
│  │  │  └─ cb1daabb2283a09cce1bfe4ab1a068eecc69c6
│  │  ├─ e1
│  │  │  ├─ 7c06fbcfb1b547b84c884ea7febba2ce9775ed
│  │  │  └─ d1641ebcba848c99673adfd98cd1ba41d7c471
│  │  ├─ e3
│  │  │  └─ 9ea0d23dbf6b89030e2d1b30a815c840d3c08c
│  │  ├─ e4
│  │  │  ├─ 161467df4b88a72b8ddfb692f93dd4fd8bff8c
│  │  │  ├─ 233f26b62bb359a7119413d271b5e517b1cb8e
│  │  │  ├─ 634b691e678ab7a972672f88863ee647ea348b
│  │  │  └─ d83a86a0cb5eb3917266ec22970609e192452b
│  │  ├─ e5
│  │  │  └─ 4bcad15e9e78cf74105047fe30b5d7e493a51c
│  │  ├─ e6
│  │  │  ├─ 4bb007e89ce3436b1806873a31ffa9780b6af1
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ e7
│  │  │  └─ 322fe5eec4d24f9838884246a11713ebb2ea67
│  │  ├─ e8
│  │  │  └─ d2f87a60fb0e27ecd7d5e2f900b499bbe8f1ca
│  │  ├─ ea
│  │  │  └─ eea727a7a72f515e58fd0563ebd661fd016ed3
│  │  ├─ eb
│  │  │  ├─ 43ccf28cce14cc63cbb09666f942079c4cb8b6
│  │  │  ├─ 6a775cf643d129f57706f1a34642585210186f
│  │  │  └─ 776f3730378733373272f01373b9e04db745af
│  │  ├─ ec
│  │  │  └─ f6c47aa359a4d4a000d3107bac594b3ac29ce6
│  │  ├─ ed
│  │  │  └─ 07816fd9915fc66eb05471fb8ce29217fb1a66
│  │  ├─ ef
│  │  │  └─ a2c0ad252591cdebfaaacfa0d330b1454525e2
│  │  ├─ f2
│  │  │  ├─ 3a9f95cd69778822b6295a820a7bf11839995f
│  │  │  ├─ 5b2c2e10b9baa1c79c1f1f9997a90fb2cf2eca
│  │  │  └─ 5f1f14b3a709c58ad311f62ca86b32f0fc3965
│  │  ├─ f3
│  │  │  ├─ 48e07cf9b7564576b12064276757b4b3f2ec18
│  │  │  └─ 48e535fd9616e0cf4638bce99ed1844018ac81
│  │  ├─ f4
│  │  │  └─ 66f1bc2bee4101600ca7d2e74bbcdf7b9bafa6
│  │  ├─ f8
│  │  │  ├─ 049763e783a008ad4f809657842d4464f3b7bd
│  │  │  ├─ 5cd8fff37ee06250861479be4890c49509a8e1
│  │  │  └─ fd424afe2b71cf6fa513b8ac438349e89747ad
│  │  ├─ fa
│  │  │  └─ b0c1f8faeb921600a23a50aa08b8e6522f0567
│  │  ├─ fc
│  │  │  ├─ 17179bfd0dd336a6cd1026b505ea3d562587d5
│  │  │  └─ 37f3b0a0205ef3ee6ff4662de4f2eccc982f35
│  │  ├─ fe
│  │  │  ├─ 0456c3b50148decc2b6897897496a6f9f2d338
│  │  │  ├─ 600a8555b446c42108d584998ac4bfa658472d
│  │  │  └─ 9c6c516f75d173713d90a2975dc7eec5d451b8
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-0c81669410dd1041a4b3a94d78b23fdc592fa5cc.idx
│  │     ├─ pack-0c81669410dd1041a4b3a94d78b23fdc592fa5cc.pack
│  │     ├─ pack-410ae87fbdde335f15e13231a8af9d496bee410c.idx
│  │     └─ pack-410ae87fbdde335f15e13231a8af9d496bee410c.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ master
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ master
│     └─ tags
├─ .gitignore
├─ Pipfile
├─ Pipfile.lock
├─ README.md
└─ ecommerce_project
   ├─ .DS_Store
   ├─ ecommerce_project
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   ├─ manage.py
   ├─ requirements.txt
   ├─ static
   └─ store
      ├─ .DS_Store
      ├─ __init__.py
      ├─ admin.py
      ├─ apps.py
      ├─ context_processors.py
      ├─ forms.py
      ├─ migrations
      │  ├─ 0001_initial.py
      │  ├─ 0002_auto_20210813_1300.py
      │  ├─ 0003_cart_cartitem.py
      │  ├─ 0004_auto_20210814_1055.py
      │  ├─ 0005_order_orderitem.py
      │  ├─ 0006_auto_20210814_1750.py
      │  └─ __init__.py
      ├─ models.py
      ├─ static
      │  ├─ .DS_Store
      │  └─ assets
      │     ├─ .DS_Store
      │     ├─ css
      │     │  ├─ animate.css
      │     │  ├─ base.css
      │     │  ├─ cart.css
      │     │  ├─ icofont.min.css
      │     │  ├─ ionicons.min.css
      │     │  ├─ jquery-ui.min.css
      │     │  ├─ magnific-popup.css
      │     │  ├─ nice-select.css
      │     │  ├─ owl.carousel.min.css
      │     │  ├─ pe-icon-7-stroke.css
      │     │  ├─ slick.css
      │     │  └─ style.css
      │     ├─ img
      │     │  ├─ .DS_Store
      │     │  ├─ bg
      │     │  │  └─ hero-bg.jpg
      │     │  ├─ icon
      │     │  ├─ logo
      │     │  │  ├─ let.png
      │     │  │  ├─ logo-let.png
      │     │  │  └─ logo.png
      │     │  └─ others
      │     │     ├─ amc.png
      │     │     ├─ circle-icon-basket.png
      │     │     ├─ elefments.png
      │     │     ├─ glob_prod_img.png
      │     │     └─ new-logo.png
      │     ├─ js
      │     │  ├─ ajax-mail.js
      │     │  ├─ jquery-ui.min.js
      │     │  ├─ jquery.magnific-popup.min.js
      │     │  ├─ jquery.nice-select.js
      │     │  ├─ jquery.scrollup.min.js
      │     │  ├─ jquery.zoom.min.js
      │     │  ├─ mailchimp-ajax.js
      │     │  ├─ main.js
      │     │  ├─ owl.carousel.min.js
      │     │  ├─ slick.min.js
      │     │  ├─ vendor
      │     │  │  ├─ jquery-3.6.0.min.js
      │     │  │  ├─ jquery-migrate-3.3.2.min.js
      │     │  │  └─ modernizr-3.11.2.min.js
      │     │  └─ wow.min.js
      │     └─ scss
      │        ├─ _common.scss
      │        ├─ _variabls.scss
      │        ├─ section
      │        │  ├─ _404.scss
      │        │  ├─ _about.scss
      │        │  ├─ _banner.scss
      │        │  ├─ _blog-details.scss
      │        │  ├─ _blog.scss
      │        │  ├─ _cart.scss
      │        │  ├─ _checkout.scss
      │        │  ├─ _compare.scss
      │        │  ├─ _contact.scss
      │        │  ├─ _faq.scss
      │        │  ├─ _footer.scss
      │        │  ├─ _header.scss
      │        │  ├─ _home2.scss
      │        │  ├─ _login-register.scss
      │        │  ├─ _my-account.scss
      │        │  ├─ _other.scss
      │        │  ├─ _product.scss
      │        │  ├─ _quick-view.scss
      │        │  └─ _wishlist.scss
      │        └─ style.scss
      ├─ templates
      │  ├─ about.html
      │  ├─ base.html
      │  ├─ cart.html
      │  ├─ contact.html
      │  ├─ contact_success.html
      │  ├─ email
      │  │  ├─ .DS_Store
      │  │  ├─ email.html
      │  │  └─ email3.html
      │  ├─ footer.html
      │  ├─ home.html
      │  ├─ navbar.html
      │  ├─ order_detail.html
      │  ├─ orders_list.html
      │  ├─ product.html
      │  ├─ signin.html
      │  ├─ signup.html
      │  └─ thankyou.html
      ├─ tests.py
      ├─ urls.py
      └─ views.py

```