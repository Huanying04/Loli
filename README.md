<img align="right" src="https://user-images.githubusercontent.com/59917505/120065193-a1664080-c0a2-11eb-8e9e-394b8d2e4800.png" height="200" width="200">

# Loli
Loli屬於一種深奧的程式語言。主要是用於讓程式碼看起來像是蘿莉的一天，或日常、日記等。

# 語法/指令
* **Awake** - 醒來。每個程式的第一行都必須寫上。不然就會拋出錯誤。
* **Sleep** - 睡覺。讀到這行程式就會直接結束。若是整個原始碼都沒包含這一行的話會顯示提醒，但不會拋出錯誤。
* **Say X** - 在螢幕上顯示X。若是含空格必須使用英文雙引號`"`刮起來。其中的Escape sequence包含`\n`、`\t`、`\r`、`\b`、`\0`、`\\`、`\'`、`\"`。
* **Put V into school bag** - 把X放進書包。宣告一個變數名為V，必須皆為ASCII字元。預設值為其所有字元所代表的數字相加。除了下述表格，其餘可顯示字元值皆為1，不可顯示字元值皆為0，並且英文大小寫值相同。儲存格式為float。

| 字元 | 值 | 字元 | 值 | 字元 | 值 |
|------|----|------|----|------|----|
| 0    | 1  | a    | 8  | n    | 6  |
| 1    | 1  | b    | 1  | o    | 7  |
| 2    | 1  | c    | 2  | p    | 1  |
| 3    | 1  | d    | 4  | q    | 1  |
| 4    | 1  | e    | 12 | r    | 5  |
| 5    | 1  | f    | 2  | s    | 6  |
| 6    | 1  | g    | 2  | t    | 9  |
| 7    | 1  | h    | 6  | u    | 2  |
| 8    | 1  | i    | 6  | v    | 1  |
| 9    | 1  | j    | 1  | w    | 2  |
|      |    | k    | 1  | x    | 1  |
|      |    | l    | 4  | y    | 2  |
|      |    | m    | 2  | z    | 1  |

* **Take out V from school bag** - 將V從書包裡拿出，做為之後程式的準備。只有已拿出的變數才能操作。
* **Speak V** - 在螢幕上顯示變數V的儲存值。
* **Show V** - 同上。
* **Clearly speak V** - 在螢幕上顯示變數V的儲存值的int值。
* **Simply speak V** - 同上。
* **Clearly show V** - 同上。
* **Simply show V** - 同上。
* **Call V** - 在螢幕上顯示變數V的儲存值所對應的unicode字元。
* **Have V** - 等待使用者輸入值，並且儲存進變數名稱為V。預設為已準備好。輸入值格式若不是float時，則將每個字元的Unicode值相加儲存。
* **Take V** - 同上。
* **Go to P** - 前往地點P。P可為任意字串。但程式結束執行時，地點必須為`Home`，大小寫不敏感。
* **Go P** - 同上。
* **Dump V** - 丟棄V。將已拿出書包的變數V刪掉。
* **Eat V** - 吃掉V。功能同上。
* **Drink V** - 喝掉V。功能同上。
* **Replace V1 with V2** - 用V2取代V1。相當於`V1 = V2`。
* **Throw away V1 and replace with V2** - 同上。
* **Add V1 to V2** - 把A加進B裡。相當於`V2 = V2 + V1`。
* **Add A and B together into C** - 把A和B加在一起變成C。創建C變數，其值為A的儲存值+B的儲存值。若是C已存在則拋出錯誤。
* **Mix A and B together into C** - 把A和B攪拌加在一起變成C。功能同上。
* **Put A and B together into C** - 把A和B放加在一起變成C。功能同上。
* **Take V1 out of V2** - 從V2拿出V1。將V2的儲存值減去V1，相當於`V2 = V2 - V1`。
* **Drop V1 out of V2** - 從V2弄掉V1。功能同上。
* **Drop V1 from V2** - 從V2弄掉V1。功能同上。
* **Give out V1 from V2** - 從V2拿出V1給別人。功能同上。
* **Slice V1 into N1 C and take N2** - 將V1切N1塊並取走其中N2塊。N1和N2為固定數字也可為變數，C為任意量詞，另外N2不得大於N1。
* **Cut V1 into N1 C and take N2** - 同上。
* **Split V1 into N1 C and take N2** - 同上。
* **Keep V** - 當V不等於0時，重複Keep下述部分，直到V=0時結束執行。Keep下述每行都必須空Keep之後一個Tab，包含空白行。
* **Fuck** - 當程式讀到某行含fuck字樣的時候，直接拋出錯誤。原因很簡單，因為你不能X蘿莉。

其餘未寫在上面的指令都不會執行，因此你可以在原始碼裡隨意放上無關的字樣也無所謂。

# 已知bug
* ~~Keep裡面不能放Keep。~~ 2021/05/29修正

# 範例
## Hello world!
**簡單的版本**
```loli
Awake
Say "Hello world!\n"
Sleep
```
**生活只剩上學的版本(?)**
```loli
Awake

Say "Hello world!\n" to the world

Put books into school bag
Put lunch into school bag

Go to school

In class
Take out books from school bag
Learning
Learning
Learning

Take out lunch from school bag
Eat lunch

Nap

Learning
Learning
Learning

Put books into school bag

Go Home
Shower

Sleep
```

## 非負整數乘法
由於Loli不自帶乘法，因此必須使用額外方式完成。
```loli
Awake

Take lollipop
Take strawberry

Put chocolate into school bag

Go to school

Take out chocolate from school bag

Replace chocolate with strawberry
Keep lollipop
	Add chocolate to strawberry
	Drop 1 from lollipop

Drop chocolate out of strawberry
Show strawberry

Go home

Sleep
```

## 計算機
可計算四則運算
```loli
Awake

Take paper
Take pigment
Take fragment

Put uwu water into school bag
Take out uwu water from school bag

Put folder into school bag
Take out folder from school bag
Drop folder from folder
Drop uwu water from folder
Replace uwu water with folder
Drop uwu water from folder

Add uwu water to pigment

Keep pigment
	Drop 1 from pigment
	Keep pigment
		Drop bb from pigment
		Keep pigment
			Cut paper into fragment shape and take 1
			Show paper
			Sleep
		Drop fragment from paper
		Show paper
		Sleep
	Add paper to fragment
	Show fragment
	Sleep

Keep fragment
	Add paper to folder
	Drop 1 from fragment
Show folder

Sleep
```

## [Truth Machine](https://esolangs.org/wiki/Truth-machine )
```loli
Awake

Put b into school bag
Take out b from school bag

Take input

Slice input into 2 parts and take 1
Add b and input together into whatever

Keep input
	Clearly show input
	Replace input with whatever

Clearly show input

Sleep
```

## 費氏數列
```loli
Awake

Take purse

Put $ into school bag
Take out $ from school bag

Put % into school bag
Take out % from school bag

Put Mif into school bag
Take out Mif from school bag

Drop $ out of purse
Drop % out of purse

Clearly show $
Call Mif
Clearly show %
Call Mif

Keep purse
	Add $ and % together into delicious thing
	Replace $ with %
	Replace % with delicious thing
	Clearly show delicious thing
	Eat delicious thing
	Call Mif
	Drop 1 from purse

Sleep
```

## [Disan Count](https://esolangs.org/wiki/Disan_Count )
```loli
Awake

Take book

Put zero into school bag
Take out zero from school bag
Drop zero from zero

Put chocolate into school bag
Take out chocolate from school bag
Replace chocolate with book
Drop chocolate from zero
Replace chocolate with zero
Add zero and book together into another book
Replace zero with another book
Dump another book

Put b into school bag
Take out b from school bag

Put cake into school bag
Take out cake from school bag
Replace cake with b

Keep chocolate
	Add chocolate and book together into chocolate book
	
	Put strawberry book into school bag
	Take out strawberry book from school bag
	Replace strawberry book with chocolate book
	
	Keep chocolate book
		Slice cake into b parts and take -1
		Drop b from chocolate book
	
	Add cake and b together into blueberry cake
	Replace cake with blueberry cake
	Eat blueberry cake
	
	Keep cake
		Clearly show strawberry book
		Say " is even!"
		Drop b from cake
		Drop b from cake
	
	Replace cake with b
	
	Add chocolate and b together into blueberry chocolate
	Replace chocolate with blueberry chocolate
	Eat blueberry chocolate
	
	Eat chocolate book
	Eat strawberry book

Sleep
```

## 99 Bottles of Beer
```loli
Awake

Put ou programming language into school bag
Take out ou programming language from school bag

Put 1 into school bag
Take out 1 from school bag

Put ca into school bag
Take out ca from school bag

Put whatever into school bag
Take out whatever from school bag

Keep ou programming language
	Clearly show ou programming language
	Say " bottles of beer on the wall, "
	
	Clearly show ou programming language
	Say " bottles of beer."
	
	Call ca
	
	Say "Take one down, pass it around, "
	
	Drop 1 from ou programming language
	Clearly show ou programming language
	Say " bottles of beer on the wall."
	
	Call ca
	Call ca

Sleep
```

## 被FBI抓走(FBIError)
```loli
Awake

Be fucked

Sleep
```
