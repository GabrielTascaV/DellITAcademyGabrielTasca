import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;



public class App{
    public static void main(String[]args) throws FileNotFoundException{
        try{
        File file = new File("TA_PRECO_MEDICAMENTO.csv");
        Scanner reader = new Scanner(file);
        ArrayList<String[]> dados = new ArrayList<String[]>();
        int contador = 0;
        while(contador<100){

            String linha = reader.nextLine();
            String linhaCortada[] = linha.split(";");
            dados.add(linhaCortada);
            contador++;
        }
        for(int i = 0; i < dados.size(); i++){
            System.out.println(dados.get(i).length);
            if(dados.get(i).length > 50){
                //System.out.println(i);
            }
        }
        reader.close();
        }
    catch(FileNotFoundException e){
        System.out.println("Arquivo não encontrado");
        e.printStackTrace();
    }
    } 
}