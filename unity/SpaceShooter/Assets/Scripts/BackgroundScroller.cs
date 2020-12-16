using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BackgroundScroller : MonoBehaviour
{
    [SerializeField]
    private float scrollspeed = 0.05f;
    private Vector2 offset;
    private Material bgMaterial;

    void Start()
    {
        bgMaterial = GetComponent<Renderer>().material;
        offset = new Vector2(0f, scrollspeed);
    }

    // Update is called once per frame
    void Update()
    {
        bgMaterial.mainTextureOffset += offset * Time.deltaTime;
    }
}
