'''
>>거스름돈 개요
    드디어 원택님은 왕국 건설 후 왕이 돼.
    정치스타일은 한국과 비슷하게 하기로함.(단, 화폐 단위 포함)

    -동전과 지폐의 단위에서 재밌는일(이 왕국에서 정해진 일)
    성질(1) : 각 단위가 바로 작은 단위로 나누어 떨어진다는것.
    ex) 500은 100의 배수이고, 100은 50의 배수이다.

    -문제 발생
    가게 운영중 거스름돈을 받아야 하는데, 점원이 못햐
    -> 거스름돈 계산 프로그램 만들자
    (특히, 동전의 수를 최소화하자.)
   '''
if __name__=="__main__":
    result=""
    #24원짜리 동전을 2개 주고 나머지를 모두 하나씩 주자.
    count_coin=0
    #동전개수
    count = 0
    now = 0#새입력
    n=int(input(":"))
    coins=list()
    for num in range(n):
        count_coin=int(input(":"))
        #동전개수
        for x in range(count_coin):
            coins.append(x)
        current_num=int(input(':'))
    while True:
        if current_num > 0:
            break
        if now == 0 or current_num - now < 0:
            now = coins.pop()
            current_num -= now
        count+=1
        result = count
    print(result)
    #숫자를 입력받자
    #입력받은 순
'''
>>입력

테스트 케이스의 첫 줄에는 왕국에서 사용하는 
동전의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 각 동전의 가치 ci(1 ≤ ci ≤ 1,000,000,000)가 
오름차순으로 주어진다. 
이때 각 동전의 가치는 
바로 다음에 오는 동전의 가치의 약수라는 성질이 보장된다. 
즉, 모든 1 ≤ i ≤ N-1에 대해 ci는 ci+1의 약수이다. 
마지막 줄에는 거스름돈의 양 K(1 ≤ K ≤ 1,000,000,000)가 
주어진다.

>>출력
각각의 테스트 케이스에 대해 최소로 필요한 동전의 수를 출력한다.
'''
'''
import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] solve = new int[n];
		for(int i = 0 ; i < n; i++) {
			int coinCnt = sc.nextInt();
			Stack<Integer> coins = new Stack<>();
			for(int j = 0; j < coinCnt; j++) {
				coins.push(sc.nextInt());
			}
			int problem = sc.nextInt();
			solve[i] = solve(coins, problem);
		}
		sc.close();
		for(int result : solve)
			System.out.println(result);
	}
	
	public static int solve(Stack<Integer> coins, int problem) {
		int cnt = 0;
		int curr = 0;
		while(problem > 0) {
			while(curr == 0 || problem - curr < 0) {
				curr = coins.pop();
			}
			problem -= curr;
			cnt++;
		}
		return cnt;
	}
}
'''