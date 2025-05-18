public class MyClass {
    private int myVar;
    protected String name;

    public MyClass() {
        this.myVar = 10;
        this.name = "Shriyansh";
    }

    private void printInfo() {
        System.out.println("Name: " + this.name);
        System.out.println("Variable: " + this.myVar);
    }

    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj.printInfo();
    }
}
