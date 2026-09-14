import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers

SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)


def load_data():
    """Load and normalize the MNIST dataset."""
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    train_images = train_images.astype("float32") / 255.0
    test_images = test_images.astype("float32") / 255.0
    train_images = train_images[..., None]
    test_images = test_images[..., None]
    return train_images, train_labels, test_images, test_labels


def split_validation(train_images, train_labels, validation_size=5000):
    """Create a validation set from the training data."""
    x_val = train_images[-validation_size:]
    y_val = train_labels[-validation_size:]
    x_train = train_images[:-validation_size]
    y_train = train_labels[:-validation_size]
    return x_train, y_train, x_val, y_val


def build_model(filters=32, dense_units=128, learning_rate=1e-3):
    """Simple CNN using only Conv2D, MaxPooling2D, Flatten, and Dense layers."""
    inputs = tf.keras.Input(shape=(28, 28, 1))
    x = layers.Conv2D(filters, (3, 3), activation="relu", padding="same")(inputs)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(filters * 2, (3, 3), activation="relu", padding="same")(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Flatten()(x)
    x = layers.Dense(dense_units, activation="relu")(x)
    outputs = layers.Dense(10, activation="softmax")(x)

    model = tf.keras.Model(inputs, outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def tune_hyperparameters(x_train, y_train, x_val, y_val):
    """Try a few model sizes and keep the best validation accuracy."""
    candidates = [
        {"filters": 16, "dense_units": 64, "learning_rate": 1e-3},
        {"filters": 32, "dense_units": 128, "learning_rate": 1e-3},
        {"filters": 32, "dense_units": 256, "learning_rate": 5e-4},
        {"filters": 64, "dense_units": 128, "learning_rate": 1e-4},
    ]

    best_result = None
    best_history = None
    data_augmentation = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.05,
        height_shift_range=0.05,
    )

    for config in candidates:
        model = build_model(**config)
        generator = data_augmentation.flow(x_train, y_train, batch_size=64)
        history = model.fit(
            generator,
            epochs=4,
            validation_data=(x_val, y_val),
            verbose=0,
        )
        val_accuracy = history.history["val_accuracy"][-1]
        if best_result is None or val_accuracy > best_result["val_accuracy"]:
            best_result = {**config, "val_accuracy": float(val_accuracy)}
            best_history = history.history

    print("\nBest hyperparameter set:")
    for key, value in best_result.items():
        print(f"  {key}: {value}")

    return best_result, best_history


def plot_training_history(history):
    """Plot training and validation accuracy/loss."""
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(history.history["loss"], label="Train loss")
    plt.plot(history.history["val_loss"], label="Validation loss")
    plt.title("Loss over epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history["accuracy"], label="Train accuracy")
    plt.plot(history.history["val_accuracy"], label="Validation accuracy")
    plt.title("Accuracy over epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()

    plt.tight_layout()
    plt.savefig("training_history.png")
    plt.close()


def plot_predictions(model, test_images, test_labels, limit=12):
    """Show some model predictions on test digits."""
    predictions = model.predict(test_images[:limit], verbose=0)
    predicted_labels = np.argmax(predictions, axis=1)

    fig, axes = plt.subplots(3, 4, figsize=(12, 9))
    axes = axes.flatten()

    for i in range(limit):
        ax = axes[i]
        image = test_images[i].squeeze()
        true_label = int(test_labels[i])
        pred_label = int(predicted_labels[i])
        ax.imshow(image, cmap="gray")
        ax.set_title(f"True: {true_label}\nPred: {pred_label}", fontsize=10)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("digit_predictions.png")
    plt.close()


def main():
    print("Loading MNIST data...")
    train_images, train_labels, test_images, test_labels = load_data()
    x_train, y_train, x_val, y_val = split_validation(train_images, train_labels, validation_size=5000)

    print("Tuning hyperparameters...")
    best_config, _ = tune_hyperparameters(x_train, y_train, x_val, y_val)

    print("\nTraining final model...")
    final_model = build_model(**best_config)
    data_augmentation = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.05,
        height_shift_range=0.05,
    )

    train_generator = data_augmentation.flow(x_train, y_train, batch_size=64)
    history = final_model.fit(
        train_generator,
        epochs=8,
        validation_data=(x_val, y_val),
        verbose=1,
    )

    test_loss, test_accuracy = final_model.evaluate(test_images, test_labels, verbose=0)
    print(f"\nTest Accuracy: {test_accuracy:.4f}")
    print(f"Test Loss: {test_loss:.4f}")

    plot_training_history(history)
    plot_predictions(final_model, test_images, test_labels)

    print("\nSaved model artifacts:")
    print("  - training_history.png")
    print("  - digit_predictions.png")


if __name__ == "__main__":
    main()
