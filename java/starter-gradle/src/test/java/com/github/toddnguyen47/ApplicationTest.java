package com.github.toddnguyen47;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ApplicationTest {
    @Test
    public void TestTwo() {
        Application application = new Application();

        Assertions.assertEquals(2, application.returnTwo());
    }
}
