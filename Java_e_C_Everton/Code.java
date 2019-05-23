class Main {
  public static void main(String[] args) {
    for (int i = 1; i <= 50; i++){
      if(i%2==0){
        System.out.printf("%d par.\n", i);
      }else{
        System.out.printf("%d impar.\n", i);
      }
    }
    
    int i = 1;
    while(i <= 50){
      if(i%2==0){
        System.out.printf("%d par.\n", i);
      }else{
        System.out.printf("%d impar.\n", i);
      }
      i++;
    }
  }
}
