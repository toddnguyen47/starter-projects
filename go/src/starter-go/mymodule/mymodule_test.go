package mymodule_test

// Run ginkgo with:
// go run github.com/onsi/ginkgo/ginkgo

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/toddnguyen47/starter-projects/go/starter-go/mymodule"
)

var _ = Describe("Mymodule", func() {
	When("The return_two() function runs", func() {
		It("returns 2", func() {
			Expect(mymodule.ReturnTwo()).To(BeEquivalentTo(2))
		})
	})
})
