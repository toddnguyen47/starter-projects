package com.github.toddnguyen47;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class ApplicationTest {
  @Test
  void testTwo() {
    final Application application = new Application();

    Assertions.assertEquals(2, application.returnTwo());
  }
}
