package main

import (
	"fmt"
	"syscall/js"
)

var count = 0

func incWrapper() js.Func {
	return js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		fmt.Println("increment")
		jsDoc := js.Global().Get("document")
		output := jsDoc.Call("getElementById", "int")
		count += 1
		output.Set("innerHTML", count)
		return count
	})
}

func decWrapper() js.Func {
	return js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		fmt.Println("decrement")
		jsDoc := js.Global().Get("document")
		output := jsDoc.Call("getElementById", "int")
		count -= 1
		output.Set("innerHTML", count)
		return count
	})
}

func resetWrapper() js.Func {
	return js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		fmt.Println("reset")
		jsDoc := js.Global().Get("document")
		output := jsDoc.Call("getElementById", "int")
		count = 0
		output.Set("innerHTML", count)
		return count
	})
}

func main() {
	fmt.Println("Go Web Assembly")
	js.Global().Set("incFunc", incWrapper())
	js.Global().Set("decFunc", decWrapper())
	js.Global().Set("resetFunc", resetWrapper())
	<-make(chan bool)
}