// Main class demonstrating polymorphism
public class Main {
    
    public static void main(String[] args) {
        
        // Creating an array of SevenWonders references (parent class type)
        // But actual objects are of different subclasses (polymorphism)
        SevenWonders[] wonders = new SevenWonders[7];
        
        // Instantiating each subclass object
        wonders[0] = new GreatPyramidOfGiza();
        wonders[1] = new HangingGardensOfBabylon();
        wonders[2] = new TempleOfZeus();
        wonders[3] = new ColossusOfRhodes();
        wonders[4] = new LighthouseOfAlexandria();
        wonders[5] = new MausoleumAtHalicarnassus();
        wonders[6] = new GreatWallOfChina();
        
        // Display header
        System.out.println("\n\n");
        System.out.println("╔══════════════════════════════════════════════════════╗");
        System.out.println("║     EXPLORING THE SEVEN WONDERS OF THE WORLD         ║");
        System.out.println("║           Using Polymorphism in Java                 ║");
        System.out.println("╚══════════════════════════════════════════════════════╝");
        System.out.println("\n");
        
        // Polymorphic call: Iterating through array and calling displayWonder()
        // Each reference automatically calls the correct subclass method
        for (int i = 0; i < wonders.length; i++) {
            // This is polymorphism - the same method call displays different info
            // based on the actual object type at runtime
            wonders[i].displayWonder();
        }
        
        // Display footer
        System.out.println("╔══════════════════════════════════════════════════════╗");
        System.out.println("║      All Seven Wonders have been displayed!          ║");
        System.out.println("║                  Thank You!                           ║");
        System.out.println("╚══════════════════════════════════════════════════════╝\n");
    }
}
