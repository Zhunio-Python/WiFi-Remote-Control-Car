package com.zhunio.picar;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputMethodManager;
import android.widget.EditText;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends AppCompatActivity implements Commands {
    private String BASE_URL = "http://";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Lookup text fields
        EditText hostTextField = (EditText) findViewById(R.id.host);
        EditText portTextField = (EditText) findViewById(R.id.port);

        setOnEditorActionListener(hostTextField);
        setOnEditorActionListener(portTextField);
    }
    public void moveForward(View view) {
        initiateThread(MOVE_FORWARD);
    }
    public void moveBackward(View view) {
        initiateThread(MOVE_BACKWARD);
    }
    public void moveRight(View view) {
        initiateThread(MOVE_RIGHT);
    }
    public void moveLeft(View view) {
        initiateThread(MOVE_LEFT);
    }
    public void cleanup(View view) {
        initiateThread(CLEANUP);
    }
    private void initiateThread(String direction) {
        try {
            Thread thread = new Thread(() -> sendRequest(direction));
            thread.start();
        } catch (IllegalStateException illegalState) {
            System.err.println("IllegalStateException: " + illegalState.getMessage());
            System.err.println("Thread was already started.");
        }
    }
    private void sendRequest(String direction) {
        try {
            URL url;

            if (direction.equals(INIT))
                url = new URL(BASE_URL + INIT);
            else if (direction.equals(CLEANUP))
                url = new URL(BASE_URL + CLEANUP);
            else if (direction.equals(MOVE_FORWARD))
                url = new URL(BASE_URL + MOVE_FORWARD);
            else if (direction.equals(MOVE_BACKWARD))
                url = new URL(BASE_URL + MOVE_BACKWARD);
            else if (direction.equals(MOVE_RIGHT))
                url = new URL(BASE_URL + MOVE_RIGHT);
            else if (direction.equals(MOVE_LEFT))
                url = new URL(BASE_URL + MOVE_LEFT);
            else
                throw new IllegalArgumentException("Not valid direction: " + direction);

            HttpURLConnection http = (HttpURLConnection) url.openConnection();
            System.out.println("FLAG 2");
            int responseCode = http.getResponseCode();
            System.out.println("Connection made: " + responseCode);

        } catch (MalformedURLException urlException) {
            System.err.println("MalformedURLException: " + urlException.getLocalizedMessage());
        } catch (IOException iOException) {
            System.err.println("Caught IOException: " + iOException.getMessage());
        } catch (Exception e) {
            System.err.println("Caught Exception: " + e.getMessage());
        }
    }
    private void hideInputManager() {
        InputMethodManager inputManager = (InputMethodManager)
                getSystemService(Context.INPUT_METHOD_SERVICE);
        inputManager.hideSoftInputFromWindow(
                getCurrentFocus().getWindowToken(), inputManager.HIDE_NOT_ALWAYS);
    }
    private void setOnEditorActionListener(EditText textField) {
        textField.setOnEditorActionListener((textView, actionId, event) -> {
            boolean handled = false;

            if (actionId == EditorInfo.IME_ACTION_NEXT) {
                BASE_URL += textView.getText().toString() + ":";
                hideInputManager();
                handled = true;
            } else if (actionId == EditorInfo.IME_ACTION_DONE) {
                BASE_URL += textView.getText().toString();
                System.out.println(BASE_URL);
                hideInputManager();
                initiateThread(INIT);
                handled = true;
            }

            return handled;
        });
    }
}
