public class Calculadora {
	
	public int soma(String expressao){ //("1+4+2+1")
		int sum = 0;
		for(String itemsoma: expressao.split("\\+")){
			sum += Integer.valueOf(itemsoma);
		}
		return sum;
	}
	public int subtracao(String expressao1){ //("1-4-2-1")
		int sub = 0;
		for(String itemsubtracao: expressao1.split("\\-")){
			if(sub == 0){
				sub +=Integer.valueOf(itemsubtracao);
			}else{
				sub -=Integer.valueOf(itemsubtracao);
			}
		}
		return sub;
	}
	public int divisao(String expressao2){ //("1/4/2/1")
		int div = 0;
		try{
			for(String itemdivisao: expressao2.split("\\/")){
				if(div == 0){
					div +=Integer.valueOf(itemdivisao);
				}else{
					div /=Integer.valueOf(itemdivisao);
				}		
			}
			return div;
		} catch(ArithmeticException ex){
			system.out.print("Não divida por zero");
		}
	}
	public int multiplicacao(String expressao3){ //("1*4*2*1")
		int mult = 0;
		for(String itemmultiplicacao: expressao3.split("\\*")){
			if(mult == 0){
				mult +=Integer.valueOf(itemmultiplicacao);
			}else{
				mult *=Integer.valueOf(itemmultiplicacao);
			}		
		}
		return mult;
	}
}