package com.aranhid;

import java.io.FileInputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException, URISyntaxException {
        FileInputStream fileInputStream = new FileInputStream("register.txt");

        Scanner fileScanner = new Scanner(fileInputStream);

        HashSet<String> banned_urls = new HashSet<>();
        HashSet<String> banned_domains = new HashSet<>();
        HashSet<String> banned_ips = new HashSet<>();


        while (fileScanner.hasNext()){
            String row = fileScanner.nextLine();
            String[] rows = row.split(";");
            banned_urls.addAll(Arrays.asList(rows[1].split(",")));
            banned_domains.addAll(Arrays.asList(rows[2].split(",")));
            banned_ips.addAll(Arrays.asList(rows[3].split(",")));
        }

        fileScanner.close();
        fileInputStream.close();

        Scanner consoleScanner = new Scanner(System.in);

        System.out.print("Enter your URL: ");
        String url = consoleScanner.nextLine();
        URI uri = new URI(url);
        String domain = uri.getHost();
        String ip = "";
        try {
            ip = InetAddress.getByName(domain).toString().split("/")[1];
        }
        catch (Exception e){

        }

        if (banned_urls.contains(url))
            System.out.println("URL is banned");
        else
            System.out.println("URL is not banned");

        if (banned_domains.contains(domain))
            System.out.println("Domain is banned");
        else
            System.out.println("Domain is not banned");

        if (!ip.isEmpty()) {
            if (banned_ips.contains(ip))
                System.out.println("IP is banned");
            else
                System.out.println("IP is not banned");
        }
        else System.out.println("Could not find ip");
    }
}
