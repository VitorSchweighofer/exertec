import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class CalculadoraTest {
	@Test
	public void avaliaExpressao(){
		Calculadora calculadora = new Calculadora();
		int sum  = calculadora.soma("1+2+3");
		assertEquals(6, sum);
	}
	@Test
	public void avaliaExpressao1(){
		Calculadora calculadora = new Calculadora();
		int sub  = calculadora.subtracao("3-1-1");
		assertEquals(1, sub);
	}
	@Test
	public void avaliaExpressao2(){
		Calculadora calculadora = new Calculadora();
		int div  = calculadora.divisao("100/1/0");
		assertEquals(0, div);
	}
	@Test
	public void avaliaExpressao3(){
		Calculadora calculadora = new Calculadora();
		int mult  = calculadora.multiplicacao("2*4*10");
		assertEquals(80, mult);
	}
}
