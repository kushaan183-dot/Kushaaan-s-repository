class Wonders7 {
	void displayInformation() {
		System.out.println("The Seven Wonders of the Ancient World:");
	}
}

class GreatPyramidOfGiza extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Great Pyramid of Giza - Egypt");
	}
}

class HangingGardensOfBabylon extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Hanging Gardens of Babylon - Mesopotamia");
	}
}

class StatueOfZeusAtOlympia extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Statue of Zeus at Olympia - Greece");
	}
}

class TempleOfArtemisAtEphesus extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Temple of Artemis at Ephesus - Turkey");
	}
}

class MausoleumAtHalicarnassus extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Mausoleum at Halicarnassus - Turkey");
	}
}

class ColossusOfRhodes extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Colossus of Rhodes - Greece");
	}
}

class LighthouseOfAlexandria extends Wonders7 {
	@Override
	void displayInformation() {
		System.out.println("Lighthouse of Alexandria - Egypt");
	}
}

class Main {
	public static void main(String[] args) {
		Wonders7[] wonders = {
			new GreatPyramidOfGiza(),
			new HangingGardensOfBabylon(),
			new StatueOfZeusAtOlympia(),
			new TempleOfArtemisAtEphesus(),
			new MausoleumAtHalicarnassus(),
			new ColossusOfRhodes(),
			new LighthouseOfAlexandria()
		};

		for (Wonders7 wonder : wonders) {
			wonder.displayInformation();
		}
	}
}
