from thread_sqlite import exec

# テーブルの作成
exec('''
CREATE TABLE test(
    user_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name    TEXT    
    )
''')

# レコードの作成
exec('''INSERT INTO test (user_name) VALUES (?)''', 'Taro')
exec('''INSERT INTO test (user_name) VALUES (?)''', 'Jiro')
exec('''INSERT INTO test (user_name) VALUES (?)''', 'Saburo')
exec('''INSERT INTO test (user_name) VALUES (?)''', 'Shiro')
exec('''INSERT INTO test (user_name) VALUES (?)''', 'Goro')

print('ok')

