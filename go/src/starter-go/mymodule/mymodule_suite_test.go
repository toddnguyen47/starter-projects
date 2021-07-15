package mymodule_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestMymodule(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Mymodule Suite")
}
