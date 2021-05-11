- `question36.py`は、エッジを最大化するコード
- 問題の目的は、ノードを最大化する必要がある？
- サンプルが言う
  - 星の数１５・・・・・・・・・・・ノードが１５
  - 文化的交流の数２３・・・エッジが２３
- `question36.py`は、エッジが最大になるループを作成したが、不正解となった
- 問題は、「3つの星を選び、最も多くの言語が習得できる組み合わせを列挙せよ
- `question37.py`は以下の方針とする
  
1. 各ノードが持つターゲットノード一覧を作成する（他のノードと重複あってもよい）
   1. '0': target_0 =[['0', '1'], ['0', '2']]
   2. '1':
   3. '2':
   4. '3': target_3 =[['3', '1'], ['3', '2'], ['3', '4']]
   5. '4':
   6. '5': target_5 =[['5', '3'], ['5', '4']]
2. 取得したノード一覧リストを宣言し、空で初期化する
   1. get_node = []
3. nC3 の最初のノードを選択する (0, )
4. 0が持つターゲットノード一覧から、取得済みノード一覧に含まれていないノードを、取得済みノード一覧に追加する
   1. get_node.append('0')
   2. get_node.append('1')
   3. get_node.append('2')
   4. get_node: ['0', 1', '2']
5. nC3 の2番目のノードを選択する （0, 3, )
6. 3が持つターゲットノード一覧から、取得済みノード一覧に含まれていないノードを、取得済みノード一覧に追加する
   1. get_node.append('3')
   2. get_node.append('4')
   3. get_node: ['0', 1', '2', '3', '4']
7. nC3 の3番目のノードを選択する （0, 3, 5)
8. 5が持つターゲットノード一覧から、取得済みノード一覧に含まれていないノードを、取得済みノード一覧に追加する
   1. get_node.append('5')
   2. get_node: ['0', 1', '2', '3', '4', '5']
9. 取得済みノード一覧に含まれるノードの数を数える
   1. len(get_node): 6 （選択したノード3個を含む）
 