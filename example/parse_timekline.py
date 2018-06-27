import easyquotation

quotation = easyquotation.use("timekline")
resp_data = """
sz000001~min_data="\n\
date:170721\n\
0930 10.83 38731\n\
0931 10.86 51310\n\
0932 10.82 59593\n\
0933 10.83 65965\n\
0934 10.80 73232\n\
0935 10.80 83027\n\
0936 10.79 99077\n\
0937 10.78 113900\n\
0938 10.78 122493\n\
0939 10.76 133219\n\
0940 10.74 163809\n\
0941 10.73 179897\n\
0942 10.75 203475\n\
0943 10.74 211557\n\
0944 10.73 228598\n\
0945 10.73 249648\n\
0946 10.71 279037\n\
0947 10.70 301856\n\
0948 10.70 315378\n\
0949 10.74 322706\n\
0950 10.73 335210\n\
0951 10.73 343544\n\
0952 10.72 354577\n\
0953 10.73 364008\n\
0954 10.74 369378\n\
0955 10.78 378306\n\
0956 10.80 391685\n\
0957 10.85 409453\n\
0958 10.84 420770\n\
0959 10.85 436050\n\
1000 10.85 442312\n\
1001 10.88 461241\n\
1002 10.86 471480\n\
1003 10.87 482841\n\
1004 10.86 493978\n\
1005 10.85 503149\n\
1006 10.85 512874\n\
1007 10.86 519841\n\
1008 10.84 525736\n\
1009 10.84 528041\n\
1010 10.84 535041\n\
1011 10.85 542966\n\
1012 10.85 553537\n\
1013 10.85 562950\n\
1014 10.85 569093\n\
1015 10.86 572951\n\
1016 10.87 576958\n\
1017 10.86 585080\n\
1018 10.89 597974\n\
1019 10.87 603557\n\
1020 10.89 615090\n\
1021 10.89 619562\n\
1022 10.89 628483\n\
1023 10.89 636502\n\
1024 10.90 643846\n\
1025 10.89 651949\n\
1026 10.88 656857\n\
1027 10.88 660369\n\
1028 10.88 665263\n\
1029 10.89 666829\n\
1030 10.88 674723\n\
1031 10.87 677413\n\
1032 10.86 680295\n\
1033 10.86 683162\n\
1034 10.85 686858\n\
1035 10.84 692692\n\
1036 10.85 696265\n\
1037 10.86 697379\n\
1038 10.85 700497\n\
1039 10.86 707571\n\
1040 10.86 711147\n\
1041 10.87 719702\n\
1042 10.88 723572\n\
1043 10.88 725909\n\
1044 10.86 729963\n\
1045 10.87 731242\n\
1046 10.87 733552\n\
1047 10.88 735403\n\
1048 10.86 737364\n\
1049 10.87 742226\n\
1050 10.85 750478\n\
1051 10.85 752307\n\
1052 10.81 760964\n\
1053 10.81 770243\n\
1054 10.81 775029\n\
1055 10.80 786321\n\
1056 10.81 789586\n\
1057 10.81 791901\n\
1058 10.81 793433\n\
1059 10.80 795199\n\
1100 10.80 798384\n\
1101 10.80 799856\n\
1102 10.81 802635\n\
1103 10.80 804444\n\
1104 10.80 808546\n\
1105 10.81 811087\n\
1106 10.82 813718\n\
1107 10.81 815245\n\
1108 10.81 818102\n\
1109 10.81 819067\n\
1110 10.80 822845\n\
1111 10.79 827407\n\
1112 10.75 846726\n\
1113 10.80 853391\n\
1114 10.80 854501\n\
1115 10.78 859448\n\
1116 10.79 863538\n\
1117 10.78 869963\n\
1118 10.78 871523\n\
1119 10.79 875989\n\
1120 10.79 878103\n\
1121 10.79 880359\n\
1122 10.80 881317\n\
1123 10.79 882287\n\
1124 10.80 885878\n\
1125 10.81 888104\n\
1126 10.80 888958\n\
1127 10.80 889412\n\
1128 10.80 890723\n\
1129 10.80 893545\n\
1130 10.80 893716\n\
1300 10.79 896551\n\
1301 10.79 898918\n\
1302 10.79 899662\n\
1303 10.80 901291\n\
1304 10.80 902934\n\
1305 10.80 904597\n\
1306 10.80 905820\n\
1307 10.80 907397\n\
1308 10.79 908510\n\
1309 10.79 910126\n\
1310 10.79 912029\n\
1311 10.79 915717\n\
1312 10.79 917947\n\
1313 10.79 919434\n\
1314 10.80 922112\n\
1315 10.79 923034\n\
1316 10.80 925785\n\
1317 10.81 929040\n\
1318 10.81 931931\n\
1319 10.81 932998\n\
1320 10.81 934923\n\
1321 10.81 936258\n\
1322 10.81 937644\n\
1323 10.82 939806\n\
1324 10.82 941003\n\
1325 10.85 950206\n\
1326 10.87 959451\n\
1327 10.85 970072\n\
1328 10.88 974156\n\
1329 10.90 1007001\n\
1330 10.89 1014956\n\
1331 10.89 1023824\n\
1332 10.89 1027411\n\
1333 10.89 1028791\n\
1334 10.88 1033052\n\
1335 10.92 1053042\n\
1336 10.91 1058853\n\
1337 10.90 1065408\n\
1338 10.89 1068592\n\
1339 10.89 1070315\n\
1340 10.90 1074893\n\
1341 10.89 1076120\n\
1342 10.87 1087507\n\
1343 10.86 1089582\n\
1344 10.87 1091375\n\
1345 10.88 1092893\n\
1346 10.88 1094252\n\
1347 10.88 1095388\n\
1348 10.87 1096719\n\
1349 10.88 1097486\n\
1350 10.86 1099234\n\
1351 10.86 1105592\n\
1352 10.86 1108156\n\
1353 10.87 1110367\n\
1354 10.87 1112736\n\
1355 10.86 1115043\n\
1356 10.85 1116117\n\
1357 10.86 1122178\n\
1358 10.86 1123951\n\
1359 10.88 1124756\n\
1400 10.89 1130107\n\
1401 10.89 1134353\n\
1402 10.88 1144226\n\
1403 10.89 1148032\n\
1404 10.88 1151142\n\
1405 10.87 1152866\n\
1406 10.87 1156709\n\
1407 10.88 1161256\n\
1408 10.88 1163713\n\
1409 10.91 1176756\n\
1410 10.93 1201483\n\
1411 10.91 1207413\n\
1412 10.91 1209596\n\
1413 10.90 1211225\n\
1414 10.90 1213800\n\
1415 10.89 1221147\n\
1416 10.89 1223047\n\
1417 10.90 1224711\n\
1418 10.89 1225864\n\
1419 10.87 1250001\n\
1420 10.86 1252342\n\
1421 10.87 1256638\n\
1422 10.86 1258351\n\
1423 10.86 1259414\n\
1424 10.86 1263054\n\
1425 10.90 1274258\n\
1426 10.87 1275679\n\
1427 10.88 1277365\n\
1428 10.87 1278593\n\
1429 10.87 1280761\n\
1430 10.86 1286192\n\
1431 10.86 1290147\n\
1432 10.87 1298926\n\
1433 10.86 1304964\n\
1434 10.84 1309918\n\
1435 10.84 1311643\n\
1436 10.84 1316993\n\
1437 10.83 1323072\n\
1438 10.83 1329767\n\
1439 10.82 1334849\n\
1440 10.83 1348364\n\
1441 10.81 1359471\n\
1442 10.82 1364908\n\
1443 10.83 1370084\n\
1444 10.83 1372536\n\
1445 10.82 1375921\n\
1446 10.80 1389080\n\
1447 10.76 1400295\n\
1448 10.79 1407314\n\
1449 10.80 1411621\n\
1450 10.80 1416778\n\
1451 10.81 1422653\n\
1452 10.81 1428920\n\
1453 10.81 1443924\n\
1454 10.83 1451211\n\
1455 10.87 1467347\n\
1456 10.89 1476423\n\
1457 10.88 1476630\n\
1458 10.88 1476630\n\
1459 10.88 1476630\n\
1500 10.89 1501020\n\
"""
data = quotation.format_response_data(resp_data)
print(data)
