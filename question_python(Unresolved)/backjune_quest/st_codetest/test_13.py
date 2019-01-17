'''
>>크루아상 개요
    원택님은 회사에 크루아상을 먹는데, 누군가 떼어먹는지 의심됨.
    ->의심을 해결할 프로그램 만들자

    문제를 단순화하기 위해서
    열린 괄호와 닫힌 괄호로 이루어진 문자열이라고 가정.

    크루아상 처음구매시 크루아상 이루는 괄호가 모두 대응되는 짝임.
    그러나 짝이 없는 괄호가 크루아상에 존재시 의심이 확신
    (물론 일부를 먹히고도 멀쩡해보이는 크루아상 있을수있다)
'''
#입력 ( 은 No출력
#입력 ()은 Yes출력
#입력 ())는 No출력
#입력 ()))는 No출력
#>>Flow
#왼쪽괄호 들어오면 1부여
#왼쪽괄호가 들어올때 마다 +1이 되고
#오른쪽괄호 올때 마다 또 1입력

left_dict=dict() #json형태의 총 data보관함
right_dict=dict() #json형태의 총 data보관함
if __name__=="__main__":
    print("write only '(' or ')' and wanted exit is 'q'")
    #왼쪽과 오른쪽 괄호의 숫자를 count
    left_num=1
    right_num=1
    main_num=1
    re=""
    while True:   
        data=input("input : ") #사용자의 입력받기
        #입력된 data를 의심하기 시작하자. 
        main_num+=1
        #Logic is 들어오는 data 처리. 왜? 들어있는값으로 의심가능
        if data == "(":
            #키:카운터
            #값:data
            left_dict[main_num]=data
        else:
            left_dict[main_num]=" "
        print("left_dict:{}".format(left_dict))
        if data == ")":
            #키:카운터
            #값:data
            right_dict[main_num]=data
        else:
            right_dict[main_num]=" "
        print("right_dict:{}".format(right_dict))
        if data == "q": #종료 조건
            break
        
        #Logic is 의심에 대한 출력
        if left_dict[main_num] != right_dict[main_num]: #들어온 쌍이 맞지 않을 때
            print("No")
        elif left_dict[main_num] == right_dict[main_num]:
            print("Yes")
        
        
'''
>>입력
테스트 케이스의 첫 줄에는 크루아상을 괄호로 표현한 문자열 S가 주어진다.
문자열의 길이는 1,000,000을 넘지 않는다.

>>출력
각각의 테스트 케이스에 대해 크루아상이 멀쩡하면 Yes를 출력한다. 
그렇지 않은 경우 No를 출력한다.
'''
'''
import java.util.Scanner;
import java.util.Stack;

public class Main {

	static final String yes = "Yes";
	static final String no = "No";
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		String[] cases = new String[n];
		String[] solve = new String[n];
		for(int i =0; i < n; i++)
			cases[i] = sc.next();
		sc.close();
		
		for(int i = 0; i < n; i++) {
			solve[i] = solve(cases[i]);
		}
		for(String str : solve)
			System.out.println(str);
	}
	
	public static String solve(String str) {
		Stack<Character> stack = new Stack<>();
		char[] charArr = str.toCharArray();
		for(int i = 0, len = charArr.length; i< len; i++) {
			if(charArr[i] == '(') {
				stack.push('(');
			} else {
				if(stack.size() < 1)
					return no;
				else
					stack.pop();
			}
		}
		if(stack.size() > 0)
			return no;
		else
			return yes;
	}
}
'''