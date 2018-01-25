public class B17 {
	public static void print(int[] ll){
		print(ll, 0);
	}

	public static void print(int[] ll, int index){
		System.out.print(index + " ");
		index = ll[index];
		if (index == 0){
			System.out.println();
			return;
		}
		print(ll, index);
	}
	
	public static void main(String[] args){
		int step = 354;
		int stop = 50000000;
		
		int[] ll = new int[stop + 1];
		int ptr = 0;

		for (int i = 1; i <= stop; i++){

			if (i % 100000 == 0){
				System.out.println(i);
			}

			for (int j = 0; j < step; j++){
				ptr = ll[ptr];
			}
			ll[i] = ll[ptr];
			ll[ptr] = i;
			ptr = i;
		}
		
		System.out.print(ll[0]);
	}
}
