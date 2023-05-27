/*
 * Carlos A Delgado
 * 27 de Mayo de 2023
 * Implementación de un arbol
 */

public class Arbol{
  private int valor;
  private Arbol hizq;
  private Arbol hder;

  public Arbol(int valor, Arbol hizq, Arbol hder) {
    this.valor = valor;
    this.hizq = hizq;
    this.hder = hder;
  }

  public String preorden(){
    String recorrIzq="";
    String recorrDer="";
    if (this.hizq != null) {
      recorrIzq = this.getHizq().preorden();
    }
    if (this.hder != null) {
      recorrDer = this.getHder().preorden();
    }
    return (String.valueOf(this.valor)+" "+recorrIzq+" "+recorrDer).replaceAll("\\s+", " ");
  }

  public String inorden(){
    String recorrIzq="";
    String recorrDer="";
    if (this.hizq != null) {
      recorrIzq = this.getHizq().inorden();
    }
    if (this.hder != null) {
      recorrDer = this.getHder().inorden();
    }
    return (recorrIzq+" "+String.valueOf(this.valor)+" "+recorrDer).replaceAll("\\s+", " ");
  }  

  public String posorden(){
    String recorrIzq="";
    String recorrDer="";
    if (this.hizq != null) {
      recorrIzq = this.getHizq().posorden();
    }
    if (this.hder != null) {
      recorrDer = this.getHder().posorden();
    }
    return (recorrIzq+" "+recorrDer+" "+String.valueOf(this.valor)).replaceAll("\\s+", " ");
  }  

  public int getValor() {
    return valor;
  }

  public void setValor(int valor) {
    this.valor = valor;
  }

  public Arbol getHizq() {
    return hizq;
  }

  public void setHizq(Arbol hizq) {
    this.hizq = hizq;
  }

  public Arbol getHder() {
    return hder;
  }

  public void setHder(Arbol hder) {
    this.hder = hder;
  }

  
  

}
