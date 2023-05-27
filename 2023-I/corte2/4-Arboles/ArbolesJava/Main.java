public class Main {
  public static void main(String[] args) {
    Arbol objArbol = new Arbol(
      1,
      new Arbol(2,
        new Arbol(4, new Arbol(8,null,null), new Arbol(9,null,null)),
        new Arbol(5, null, null)
      ),
      new Arbol(3, 
        new Arbol(6, null,null),
        new Arbol(7, null, null)
      )
    );
    System.out.println(objArbol.getValor()); // 1
    System.out.println(objArbol.getHizq().getValor()); // 2
    System.out.println(objArbol.getHizq().getHizq().getValor()); //4
    System.out.println(objArbol.getHder().getHder().getValor()); //7
    System.out.println(objArbol.preorden());
    System.out.println(objArbol.inorden());
    System.out.println(objArbol.posorden());
    
  }
}
