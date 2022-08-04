package mymodule_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"github.com/toddnguyen47/starter-projects/go/starter-go/internal/mymodule"
)

var _ = Describe("Mymodule", func() {
	When("The return_two() function runs", func() {
		It("returns 2", func() {
			Expect(mymodule.ReturnTwo()).To(BeEquivalentTo(2))
		})
	})
})
