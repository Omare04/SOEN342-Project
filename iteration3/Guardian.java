// Guardian.java
public class Guardian {
    private String name;
    private List<Client> minors;

    public Guardian(String name) {
        this.name = name;
        this.minors = new ArrayList<>();
    }

    public void addMinor(Client minor) {
        minors.add(minor);
    }

    public String getName() {
        return name;
    }

    public List<Client> getMinors() {
        return new ArrayList<>(minors);
    }
}
