import java.util.Scanner;

public class Main {

	int M;		// 반복 인정 회수
	char[] S;	// 조사 문자열

	void inputData() {

		Scanner sc = new Scanner(System.in);

		M = sc.nextInt();
		S = (sc.next() + "\0").toCharArray();

		sc.close();
	}

	void Solve() {
		int i;			// 문자열 S의 어떤 문자를 지시
		int len;		// 문자열 S의 길이
		char r_char;	// 반복되는 문자
		int r_cnt;		// 반복 회수

		// 코드 구현 및 결과 출력
		r_cnt = 1;
		r_char = S[0];

		for( i=1; i<S.length; i++){

			if(S[i] != r_char) { // 다름 ㅋㅋ
				if(r_cnt >= M){ // 압축문 출력
					System.out.print(r_char);
					System.out.print("(");
					System.out.print(r_cnt);
					System.out.print(")");
				}
				else { // 단문 출력
					for( int v=0; v<r_cnt; v++){
						System.out.print(r_char);
					}
				}
			}
			else { // 대박. 같네
				r_cnt++;
				continue;
			}
			r_char = S[i];
			r_cnt = 1;
		}


	}

	public static void main(String[] args) {
		Main m = new Main();

		m.inputData();		//	입력 함수
		m.Solve();			//	문제 풀이
	}
}
