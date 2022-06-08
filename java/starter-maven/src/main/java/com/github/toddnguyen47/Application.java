package com.github.toddnguyen47;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Application {
  private static final Logger LOGGER = LogManager.getLogger(Application.class);

  public static void main(final String[] args) {
    LOGGER.info("Remember to change your project name!");

    LOGGER.fatal("fatal");
    LOGGER.error("error");
    LOGGER.warn("warn");
    LOGGER.info("info");
    LOGGER.debug("debug");
    LOGGER.trace("trace");
  }

  public int returnTwo() {
    return 2;
  }
}
