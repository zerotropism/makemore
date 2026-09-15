# makemore

A character-level language model, reimplemented from scratch. Follows Andrej Karpathy's
[makemore](https://github.com/karpathy/makemore), reimplemented rather than forked.

**Work in progress.** The notebook currently covers the bigram model: counting character pairs,
turning the counts into probabilities, and sampling names from them. The neural network
formulation, and everything after it, is not written yet.

If you are looking for the finished counterpart, [micrograd](https://github.com/zerotropism/micrograd)
is the same exercise carried through: an annotated autodiff engine with a trained perceptron.

## Run it

```bash
uv sync --all-groups
uv run jupyter lab notebook.ipynb
```

## Tests

```bash
uv run pytest
```
