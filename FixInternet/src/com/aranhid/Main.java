package com.aranhid;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Integer N = scanner.nextInt();
        Integer lakeID = 0;

        ArrayList<Integer> lakes = new ArrayList<>(N);
        for (int i = 0; i < N; i++){
            lakes.add(lakeID);
        }

        while (scanner.hasNextInt()){
            Integer edgeA = scanner.nextInt() - 1;
            Integer edgeB = scanner.nextInt() - 1;

            if (lakes.get(edgeA) == 0 && lakes.get(edgeB) == 0){
                lakeID++;
                lakes.set(edgeA, lakeID);
                lakes.set(edgeB, lakeID);
            }

            if (lakes.get(edgeA) == 0 && lakes.get(edgeB) != 0){
                lakes.set(edgeA, lakes.get(edgeB));
            }

            if (lakes.get(edgeA) != 0 && lakes.get(edgeB) == 0){
                lakes.set(edgeB, lakes.get(edgeA));
            }

            if (lakes.get(edgeA) != 0 && lakes.get(edgeB) != 0){
                Collections.replaceAll(lakes, lakes.get(edgeA), lakes.get(edgeB));
            }
        }

        for (int i = 0; i < lakes.size(); i++) {
            if (lakes.get(i) == 0){
                lakeID++;
                lakes.set(i, lakeID);

            }
        }

        Set<Integer> unique = new HashSet<>(lakes);

        System.out.println(unique.size() - 1);
    }
}
