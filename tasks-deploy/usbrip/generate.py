TITLE='USBrip'
STATEMENT_TEMPLATE='''
Смотрите [логи](/static/files/n7vngt3izm/{}.log)
'''

def generate(context):
    participant = context['participant']
    team_id = team_ids[participant.id % len(team_ids)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(team_id))

team_ids = ['FAuR4fBN', 'hOjj4BS0', 'gIPeF1uS', 'ZoORmGH4', 'CTYGgOOS', 'tgI3ygNy', 'oPm8aHF5', 'sxDIuRZ4', 'H5xbM4jq', '0RneVqO0', 'UqJGMuZJ', 'HwelSkL8', 'j20RzaJ4', 'sV13RZhh', '3rLEIeWT', 'Egcn608f', 'MHkar4yL', 'zflsUwR6', 'MN6xyyiE', 'C6VXMMsd', 'nN7YBx9m', 'c4TmQfjU', 'h5qqhk11', 'HjjuTp3q', 'bKf2pbLv', 'qCtHBDGV', 'cNtBqLfO', 'nDPIz34N', 'E5ZU387u', 'BOqhGkFY', 'b3wKb2VM', 'WlGRqOCI', 'TULIuQOh', 'Fu8wTYBL', 'ooYrVnhG', '7WK1ycdz', '2ffBdTmx', 'wvKoJJYa', 'f1PLQN7h', 'PktUv5Cv', '8p4fa7Lt', 'NvTx3bJG', 'vYNT9IMO', 'byCUEvOD', 'BtDWFXVC', 'xkUkCBJF', 'nW4SxkTs', 'dxYcnp6Y', 'iRldGjSB', 'I8tT3fon', 'xkRsZnOs', 'O9HtlJDc', 'ZA02IBio', 'KqQ5Zm0z', 'DKYXlFoZ', 'GazLNas6', 'hWJYgM5A', '0rlbziMz', 'ABJw3Tji', 'TNW16D9c', 'tgcmKClH', 'hp1q0iSh', 'XDOP2n18', 'UyfgEnc4', 'QMVpG6tq', 'OsC3WC2s', 'g0kPJoUl', 'DoBeli6w', 'H1qVgGyg', 'OaEv7Hpk', 'iXtw0oSn', 'sg6o0207', '1XhEoNXs', '1k1pxuWp', 'F4RQ5Xxk', 'mG01RbgW', 'xiEajJz7', '0mPoDVqA', 'de3HfS4u', 'BHxjIfDJ', 'tT3YGW2v', 'UuTcoJkG', 'Un8LXaBN', 'nFtLC1OM', 'GgANrm1j', 'k582ghlN', 'jVdFJPdX', 'b43IDjtl', 'qzDdssdS', '69R2RTXC', 'rGFkDbKN', 'eKRmnlPJ', 'KBIimsW3', 'msSPC04V', 'nYXhEEBb', 'i9nQnJKU', '2l285w3Q', 'MkGKg84Y', 'pG2DW1XS', 'Ru6a1rLE', '9mVQ5MBq', 'Gtu5ftEK', '4lJhYWqt', 'HXFsIjUl', 'pFoJjPFv', 'ijjh9kzm', '5o3ccJOg', 'methvx3o', 'WcbpACtb', 'sKHPkFkX', 'mZif2SC6', 'ou5sOV82', 'h8IJtWrp', '83l6kRXA', '7DaN0fw1', 'riO0wEec', '4qKjM8ye', 'YBt3Rr6J', 'NBCqSB2K', 'upJHRuyF', 'b36EUiSf', 'VaOChxZW', 'rkht3GRK', 'yeIuXmnr', 'C0BYqGzJ', 'sFeS97IM', 'FskkK6LL', 'F78OURne', 'EZ020CxD', 'GXqC2hxr', 'KOTfw69q', 'vjJcF6XX', '3RZ2pCaz', 'zEj5mcVY', 'emuJiMNe', 'twAdYZ81', 'Go1oepDn', 'WnoBrNbS', 'lhD4rDXt', 'mF2IXNME', 'TAr5oXB5', 'rP6LbbUZ', 'sQuBqkL5', 'eQ429UGu', 'gZy0wabt', 'nRbQpKjn', 'OmskUYcC', 'u8h2MO2w', 'fW91tG1q', 'kzh6bNvu', 'OYR9QQPU', 'U8SCSF8U', 'zgQz9TLG', 'pt4PaFfb', '80fJDHt7', 'Q43GPTFx', 'wlJWdoDC', 'sUYr4WQv', 'BgeMSZDE', 'Kz37tuhZ', '4o0dXNhj', 'liPme6EU', 'Sl2Yn0ld', '089z9Vh3', 'SYGZJosE', '804BQ5DC', 'DSnrclwN', '9J628Qaf', 'CSYusLgd', '1EY49xwT', 'bx4tff2V', 'LxLPRaLJ', '7vdjJz1m', 'jTeFagqa', 'vyl9gPwR', 'q7ppeOpR', 'OkRbdrjm', 'PnrPGiTn', 'WRnQXQ6Y', 'JJ270yYY', 'zGXiZ74Q', 'vJCHJIHN', 'nQeag53l', 'ztCZ6u22', 'IYxg72lj', 'GQLUWg7V', 'InOLnt2j', 'aCnqNJb9', 'yrIZqp0j', 'ZBAcBmII', 'qXqOkzg8', 'iFzlzNuu', 'fuFSeRKd', 'aoEsIOOS', 'LXsj9SNT', 'YiNFrT0Z', 'M97d74B8', 'vGRbtLs0', 'eWF40Ooc', '7Po6Nh56', 'PfsqkoTF', 'vvIE16ZK', 'dXRV8OIR', 'l5YLwm8T', 'aBRHYklU', 'eY5ZPktb', 'dxEfjClP', '9SINQgyC', 'n3lfumj9', 'LUNKRi3i', 'QMC3jUgE', '7g3xzGov', 'SYl0ycQA', '9mAz0byq', 'D2vzYSxS', '8R7iNr7v', 'xY8tKqtB', '009gWF9y', 'ybkbKx5F', 'nZ3EForI', 'xnRm5eg7', 'P2jBu5bq', 'IlLTuNjY', 'Cn9BOYqt', 'EqXlVndV', 'yEaRve8T', 'vKbISWoR', 'xEX4oK8u', 'CKhl8zmv', 'czA0SxFn', 'Yqd8AcT0', '24TdPbqZ', 'HLKZOj7j', 'zF3kiJQT', 'DFqDWK1s', 'LfXZ7juZ', 'yOLdVjiC', 'KjNr84eS', '9ynj49n9', '0PmCGtTJ', 'L0uXnlm5', '9vaBFXfh', 'wLGKC96u', 'FgLSoiOV', 'NOvHGsKd', 'INj5kRTK', '9KrULsvz', 'cfwfcyYZ', 'dep9gcrQ', 'r8ehfqhX', '4sn4xqis', 'ThdtcUmX', 'P0Wv8F0M', 'TMLPRxgt', 'UKJOpr6O', 'O5oiNlfV', 'rqn2Nar7', 'LjCrYy0W', '3gURHZdi', 'CeblXO9V', '5CyS8ms8', '28Ui5XJC', 'E86uZ03P', 'vzeGXMAU', 'dbXk7vgz', 'OBQxX1xZ', 'E5ZSxTQk', 'I0tdeIFa', 'cb3vProA', 'HtnhfJ6V', 'FmlvlrDy', 'UZ5Qmo78', 'C0VIQ8jO', '6cMoCNAE', '9OXbCTla', '6cj4vH0P', 'q8sWZa9h', 'ksvU0kq2', 'KAeRbgsi', 'v55mpVo1', 'W7SBfDfN', 'oBHDkWGU', 'lGKHVNte', 'l8jCIEKn', 'LEyLuCBd', 'DoyBilBq', 'Q2IWUeBz', 'hvbeU5GQ', 'PCK3s3nK', '09EZ3KfQ', 'WxylR2n0', 'GBvGNoAh', 'avxinKdp', 'IFzNP2M3', 'e2RnMZPN', 'LRuPN6FN', 'qhE2TTsH', 'CYYdObzu', 'ASb27fJs', 'MIzG8VFA', 'qXGEpTxq', 'N6Khs9n0', 'OBTQBDNi', 'umHhQBFG', 'q7b0e5IW', 'Uy5tBq5Z', 'zIDXO6Zo', 'FW7tmsrD', '764Ki0Fd', 'WnssWYOP', 'dCbQfaJp', 'faeYB3oO', 'LeI5d5iT', 'wdjqintS', 'rVc07dIx', 'xQZ3aVh8', 'NssLs8Zd', 'VqywQ4hW', 'FfaHWgw2', 'IKYXL0su', 'MSCZXwSL', 'xRsR4A7Q', '3GWsFyyW', 'lyj4LW4R', 'TUgZO8QT', 'CXweYMET', 'JO6q33GA', 'VNgOTDL3', 'ccXt2GV8', '6v9uqFrX', 'S3dp6BAv', 'epeg7zuu', '4B8IjHXF', 'vDG3kI5g', 'YIapymaD', 'slK0uvLS', 'JXVn1lIQ', 'APnPBqog', 'iE8oDVNq', 'MywRZsAU', 'xkShvDhj', 'snXhBqXA', 'YL9PivlC', 'VLeZkMP5', 'Q9maY9sE', 'Z1jvlPVX', '0PDwukFo', 'UB30qKpY', 'CQtxQrx0', 'WSFOiIhQ', 'h6gTm97U', 'KZn7i7jb', 'PoIZ3Ddv', 'uLv4YFfH', 'suz0YV3r', 'xa28q0VE', 'tXLUKBM5', 'IS5uq5Nw', 'x4eUcJ2X', 'U9NR4PJJ', 'x1nY5fv0', 'SLVOsNB0', 'oqYd07R2', 'dx3C37IA', 'DWENHA06', 'yhHPplDj', '8XUuY1Eo', 'a8028nG6', '3AXH3iT8', '6OVvCslp', 'gX5RmhFJ', 'G6Djslqp', 'WFlLtvDA', 'YcOfbUMx', '1ga6kIQj', 'd3OOvNj3', 'KSov9b7D', 'XAxXesNO', 'DK1clZUU', 'rWU2BhUE', 'lcQmEEHi', 'N8N9EMeE', 'a7oep4HV', 'WbF1CjGh', '8aC604lK', 'nyYUQ6dJ', 'FEC1gtTF', 'Zwjr6dhL', 'n3XfFHeo', 'GYdidGw5', 'cb0n5ugR', 'gktpDzr9', 'KvKwECCi', 'UfzTGyue', 'oxpMTVrJ', 'psJGCF2i', '9uFpZ0ts', '5JdGBhWm', 'GoKcnedj', 'mafHY5iI', 'aodsN2sB', 'NcG90iO6', '89t1K6Xk', 'G8e2eOhl', 'ZpfeTcE5', 'M4dmXkxO', '4JA3iH43', 'vBuICEeI', 'Ari1uObZ', 'GtD0Qhel', '5lRPVzCJ', 'hqsopbLA', 'xu6LOA8k', 'H9s29u3C', 'f7PguTGW', '3PHbMlWN', 'TpCDRXLg', 'zJbO8bkh', 'a4AuCIs6', 'EVpUcBUe', 'K8msA0Ck', 'BMnfTEiq', 'nq87fNr8', 'kzJUVYO4', 'fdfWJ2Wd', 'NR2cdHhc', 'f4gbQTfS', 'MEl6I8t4', 'IjGmb39B', 'boMQVUGP', 'm54jXiRm', '6jbvQznP', '1gWeir6G', 'c6A1OHjb', 'h3aoORf0', '6oaR0cCm', 'D15AMBuC', 'FMu9lYE5', 'nzlBGSXv', 'lm2RNZ40', 'vrh0F2d0', 'nTAh2loI', '987OAIn9', '4eCCaUSx', 'HcKglWqM', 'htWLiLn5', 'KUOGZpZ5', 'XY7hjG2q', 'od4BHPI1', 'hikF1j7v', 'THhq1uxK', 'Dbei7zyx', 'fSa44lgv', 'gkHjfA6X', 'hNtKS2UN', 'ZCiPKv16', 'BwGlpmLb', 'ArOXHGgh', 'eG0G16dg', 'jncPSptk', 'rvKsAad4', 'xmhBE1Nu', 'NG09fE6O', 'y2pldNp2', 'od9zALN6', 'mHKH3snU', 'KWm5sJHz', 'GCApeYY1', 'zlpJQ0pn', '8RsAJvfb', 'KF1NqA4b', 'D7I9FnL1', '46UsQGeY', 'FoVwzG7X', 'U8s5muqr', 'ze9yCRQt', '4GOUhgS1', 'Pb0h0Slw', 'AIUsCLqr', 'JpHWqJSh', 'oRX99Y18', '0wV3zom6', 'Yt8xZbEB', '9VgpwXzs', 'JcwuZunz', 'WSEBuzjg', 'rHA44a0J', 'RleXbk2D', 'vlIcRg3B', 'VRkaoT7y', '9DbJrXIT', 'LtXlJfc8', 'jkZ367cE', 'MsgBnGyI', 'iUcrILWH', 'qPtiqCTA', 'UlDrAyrG', 'RAu4I45F', 'CFb01F6l', 'MuGrAgwL']