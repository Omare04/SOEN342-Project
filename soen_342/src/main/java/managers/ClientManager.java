package src.main.java.managers;

import src.main.java.models.Client;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ClientManager {
    private static final String CLIENTS_FILE = "src/data/Clients.csv";

    public void registerClient(int id, String name, int age, Integer guardianId) {
        Client client = new Client(id, name, age, guardianId);
        try {
            // Convert data to CSV format and write it as a single row
            CSVManager.writeCSV(CLIENTS_FILE, Collections.singletonList(new String[]{
                    String.valueOf(id), name, String.valueOf(age), guardianId == null ? "" : String.valueOf(guardianId)
            }));
            System.out.println("Client registered successfully.");
        } catch (IOException e) {
            System.err.println("Error registering client: " + e.getMessage());
        }
    }
}