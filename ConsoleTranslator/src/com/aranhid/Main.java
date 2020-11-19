package com.aranhid;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

class Translations {
    Translations(String text){
        this.text = text;
    }

    public String text;
    public String to;
}

class ServerResponse {
    public Translations[] translations;
}

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Выберите язык, на который нужно перевести текст: ");
        String LANGUAGE = scanner.nextLine();

        System.out.print("Введите путь до файла с текстом: ");
        String PATH = scanner.nextLine();
        String FILENAME = PATH.split("\\.")[0];

        try {
            FileInputStream textFileStream = new FileInputStream(PATH);
            scanner = new Scanner(textFileStream);
        }
        catch (IOException e){
            System.out.println("Файл не найден!");
            return;
        }

        ArrayList<Translations> textToTranslate = new ArrayList<>();
        while (scanner.hasNext()) {
            String temp = scanner.nextLine();
            textToTranslate.add(new Translations(temp));
        }

        scanner.close();

        Gson gson = new Gson();

        String API_URL = "https://api.cognitive.microsofttranslator.com/translate//?api-version=3.0&to=" + LANGUAGE;
        String postData = gson.toJson(textToTranslate);

        URL url = new URL(API_URL);
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
        urlConnection.setRequestMethod("POST");
        urlConnection.addRequestProperty("Ocp-Apim-Subscription-Key", "");
        urlConnection.addRequestProperty("Ocp-Apim-Subscription-Region", "westeurope");
        urlConnection.addRequestProperty("Content-Type", "application/json");
        urlConnection.setConnectTimeout(5000);
        urlConnection.setReadTimeout(5000);

        urlConnection.setDoOutput(true);
        OutputStream out = urlConnection.getOutputStream();
        out.write(postData.getBytes());
        out.close();

        Date date = new Date();
        SimpleDateFormat formatDate = new SimpleDateFormat("yyyy-MM-dd_hh-mm-ss");
        String newFileName = FILENAME + "_" + formatDate.format(date) + ".txt";
        FileWriter writer = new FileWriter(newFileName);

        Type listType = new TypeToken<ArrayList<ServerResponse>>() {}.getType();
        ArrayList<ServerResponse> responses = new ArrayList<>();
        try {
            InputStreamReader reader = new InputStreamReader(urlConnection.getInputStream());
            responses = gson.fromJson(reader, listType);
            reader.close();
        }
        catch (IOException e){
            System.out.println(e);
            System.out.println("Вы ввели неправильный язык для перевода!");
            return;
        }

        for (ServerResponse response: responses)
        {
            for (Translations translation: response.translations)
            {
                writer.write(translation.text);
            }
            writer.append('\n');
        }
        System.out.println("Готово! Перевод находится в файле " + newFileName);
        urlConnection.disconnect();
        writer.close();
    }
}
